# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:53:55 2021

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = True  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Modello lineare
def lin(x, m=1, q=0):
    return m*x + q

vin, dvin, vout, dvout = np.genfromtxt('./data/voutvs.csv',  float, delimiter=',',
                     skip_header = 1, usecols=(0,1,2,3), unpack = True)
v_min = 0; v_max = 0.6

# Linear fit
x, y, dx, dy = mesrange(vin, vout, dx=dvin, dy=dvout,
                        x_min=v_min, x_max=v_max)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Input amplitude $V_s$ [V]', ylab=r'Output amplitude $V_{\rm out}$ [V]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [3, 0]
model = lin

deff = dy
pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Output amplitude $V_{\rm out}$ [V]')
if tix: tick(axf, xmaj=0.1, ymaj=0.2)

axr.set_xlabel(r'Input amplitude $V_s$ [V]', x=0.8)
if tix: tick(axr, xmaj=0.05, ymaj=1)
legend = axf.legend(loc='best')

# complete graph with data at opamp saturation
fig, ax = plt.subplots()
grid(ax, xlab=r'Input amplitude $V_s$ [V]', ylab=r'Output amplitude $V_{\rm out}$ [V]')
ax.errorbar(vin, vout, dvout, dvin, **lab.rc.MEASURE_MARKER)
ax.plot(x, model(x, *pars), label='Measured linear gain', zorder=5)
ax.axhline(3.90, c='r', alpha=0.5, label='Amplifier output saturation $= 3.90\pm 0.02$ V')
ax.axhline(3.90 + 2e-2, c='r', ls='--', alpha=0.3); ax.axhline(3.90 - 2e-2, c='r', ls='--', alpha=0.3)
legend = ax.legend(loc='best')