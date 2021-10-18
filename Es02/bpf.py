# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:39:19 2021

@author: berni
"""

from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Modelli di trasferimento
def lpf(f, fT=0):
    return 1./np.sqrt(1+(f/fT)**2)

def ALPF(f, fT, A=1):
    return A/np.sqrt(1+(f/fT)**2)

def hpf(f, fT):
    return 1./np.sqrt(1+(fT/f)**2) 

def band(f, fl, fh, A=1):
    return 20*np.log10(A/np.sqrt((1 + (f/fl)**2)*(1 + (fh/f)**2)))

f, CH1, CH2, phi = np.genfromtxt('./data/bpfnetgain.csv', float, delimiter=',',
                            skip_header=21, unpack=True)

# Input data manipulation
f_min = 10; f_max = 1e6
x, y, dx, dy = lab.mesrange(f, CH2, x_min=f_min, x_max=f_max)
y = 20*np.log10(y)
dx = x*1e-3; dy = 1e-2*np.abs(y)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Frequency $f$ [Hz]', ylab='Phase $\phi(f)$ $[^\circ]$')
ax.errorbar(f, phi, 1e-3*phi, 1e-2*f, 'k.', ls='-', ms=2, alpha=0.8, label='data')
ax.plot(f, (np.arctan(16.06e3/f) + np.arctan(-f/384.))*180/np.pi,
        label=r'$\tan^{-1}\frac{f_2}{f} - \tan^{-1} \frac{f}{f_1}$', zorder=5)
ax.set_xscale('log')
legend = ax.legend(loc='best')

# gain fit
init = [384, 16e3, 0.5]
model = band
par_bounds = [[0.0, 1e3], [0., 1e5], [0, 1]]
genetic_pars = lab.gen_init(model, coords=[x, y], bounds=par_bounds, unc=dy)

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm')
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# fit graphs
space = np.linspace(6, 1.2e6, 100_000)
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.plot(space, model(space, *pars), label=r'fit $\chi^2 = %.f/%d$' % (chisq, ndof))
axf.set_ylabel('Gain $A(f)$ [dB]')
if tix: lab.tick(axf, xmaj=5, ymaj=50)

axr.set_xlabel('Frequency $f$ [Hz]', x=0.8)
if True: lab.tick(axr, ymaj=1, ymin=0.2)
axf.set_xscale('log'); axr.set_xscale('log')
legend = axf.legend(loc='best')
