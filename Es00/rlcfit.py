# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 18:28:26 2021

@author: berni
"""
from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres, dosc)
import phylab as lab

def periodify(signal, cycles=1, start=0, stop=None ):
    """
    Parameters
    ----------
    signal : array_like
        Array containing a signal to be repeated for a certain number of cycles.
    cycles : int, optional
        How many copies of signal to be inserted in the output array. The default is 1.
    start : int, optional
        Start point from which to start copying the signal array. The default is 0.
    stop : int, optional
        End point at which to stop copying the signal array. The default is None
        (last element inclusive).

    Returns
    -------
     synth: ndarray
        An array containing cycles copies of the original signal periodically repeated.

    """
    synth = np.copy(signal[start:stop])
    if cycles > 1:
        synth = np.concatenate(tuple(synth for n in range(cycles)))
    return synth
    
''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

st, ch1, ch2, mh1 = np.genfromtxt('./data/rlc.csv', float, delimiter=',',  unpack=True)

t_min = 3.5e-4; t_max = 8.5e-4
t, x_a, dt, dx = lab.mesrange(st, mh1, x_min=t_min, x_max=t_max)
t_b, x_b, dt, dx = lab.mesrange(st, ch1, x_min=t_min + 8e-5, x_max=t_max)
# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, (ax1, ax2) = plt.subplots(2, 1)
grid(ax1, xlab='Time [s]', ylab='Damped oscillation $V(t)$ [V]')
grid(ax2, xlab='Time [s]', ylab='Original signal [V]')
ax1.plot(t, x_a, 'b+', ls='-', alpha=0.6)
ax2.plot(st, ch1, 'grey', marker='+', ls='-',  alpha=0.6); ax2.plot(t_b, x_b, 'b+', ls='-', alpha=0.6)

t = t - t[0]
dt = np.full(t.shape, 2e-7); dx = 2e-4*np.ones_like(x_a)

# fit damped oscillation
init_a = [1, 5e3, 0., 0, 3e-4]
model = dosc
#ax1.plot(t, dosc(t, *init_a), 'y', alpha=0.6, label='initial estimate')

pars, covm, deff = propfit(model, t, x_a, dt, dx, p0=init_a)
perr, pcor = errcor(covm)
prnpar(pars, perr, model=model)
chisq, ndof, resn, sigma = chitest(model(t, *pars), x_a, unc=deff,
                                      ddof=len(pars), gauss=True, v=True)

# graphs
fig, (axf, axr) = pltfitres(model, t, x_a, dt, deff, pars=pars)
axf.set_ylabel('RLC Signal $V(t)$ [V]' )
if tix: lab.tick(axf, xmaj=5, ymaj=50)
legend = axf.legend(loc='best')

axr.set_xlabel('Time [s]', x=0.94)
if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)
plt.show()

# Fourier transform and Quality factor estimate from FWHM
freq, tran, fres, frstd = lab.FFT(t, signal=periodify(x_a, cycles=100), window=np.kaiser, beta=None)
figfrq, (ax1, ax2) = lab.plotfft(freq, tran, norm=True, mod_ph=True, dB=True)
fwhm = lab.FWHM(freq, tran, FT=True); fmax=pars[1]
print("FWHM = %.1f Hz" %fwhm)
Qf = np.sqrt(3)*fmax/fwhm; print(f'Qf = {Qf:.1f}')