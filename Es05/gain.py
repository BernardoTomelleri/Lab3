# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:04:00 2021

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = True  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Modello lineare
def lin(x, m=1):
    return m*x

vin, dvin, vout, dvout = np.loadtxt('./data/Av5k1.txt', float, unpack=True)
vin*=1e-3; dvin*=1e-3; vout*=1e-3; dvout*=1e-3
v_min = 0; v_max = 0.6

# Linear fit
x, y, dx, dy = mesrange(vin, vout, dx=dvin, dy=dvout,
                        x_min=v_min, x_max=v_max)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Input amplitude $v_{\rm in}$ [V]', ylab=r'Output amplitude $v_{\rm out}$ [V]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [5]
model = lin

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm', max_iter=1, tail=2)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Output amplitude $v_{\rm out}$ [V]')
if tix: tick(axf, xmaj=5, ymaj=0.5)

axr.set_xlabel(r'Input amplitude $v_{\rm in}$ [V]', x=0.8)
if tix: tick(axr, xmaj=0.05, ymaj=0.1, ymin=0.02)
legend = axf.legend(loc='best')

# complete graph with data at opamp saturation
fig, ax = plt.subplots()
grid(ax, xlab=r'Input amplitude $v_{\rm in}$ [V]', ylab=r'Output amplitude $v_{\rm out}$ [V]')
ax.errorbar(vin, vout, dvout, dvin, **lab.rc.MEASURE_MARKER)
ax.plot(x, model(x, *pars), label='Measured linear gain')
ax.axhline(3.88, c='r', alpha=0.5, label='Amplifier output saturation $= 3.88 \pm 0.03$ V')
ax.axhline(3.88 + 28e-3, c='r', ls='--', alpha=0.3); ax.axhline(3.88 - 28e-3, c='r', ls='--', alpha=0.3)
legend = ax.legend(loc='best')