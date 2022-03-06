# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:53:55 2021

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions
TEMP = False

# Modello lineare
def lin(x, m=1, q=0):
    return m*x + q

time, dist, temp = np.genfromtxt('./data/railtime.csv',  float, delimiter=',',
                     skip_header=1, usecols=(0,1,3), unpack = True)
t_min = 0; t_max = 5
dt = np.ones_like(time)*0.005; ds = 15*np.ones_like(dist)
# Linear fit
x, y, dx, dy = mesrange(time, dist, dx=dt, dy=ds,
                        x_min=t_min, x_max=t_max)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'travel time $t$ [ms]', ylab=r'travel distance $s(t)$ [mm]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [3, 0]
model = lin

deff = dy
pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init, absolute_sigma=False)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'distance in air $s(t)$ [mm]')
if tix: tick(axf, xmaj=0.1, ymaj=50)
if TEMP:
    axt = axf.twinx()
    axt.errorbar(x, temp, 0.001, dx,'b.', ls='',  label='Therm data')
    axt.set_ylabel('Thermistor Voltage $V(TH)$ V')
    axt.axhline(2.69, c='r', alpha=0.5, label='Thermistor Voltage $= 2.69\pm 0.01$ V')
    axt.axhline(2.69 + 1e-3, c='r', ls='--', alpha=0.3); axt.axhline(2.69 - 1e-3, c='r', ls='--', alpha=0.3)


axr.set_xlabel(r'travel time $t$ [ms]', x=0.8)
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')