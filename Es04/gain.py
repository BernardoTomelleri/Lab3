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
def lin(x, m=1, q=0):
    return m*x + q

vin, dvin, vout, dvout = np.loadtxt('./data/Av.txt', float, unpack=True)
v_min = 0; v_max = 3

# Linear fit
x, y, dx, dy = mesrange(1e-3*vin, 1e-3*vout, dx=1e-3*dvin, dy=1e-3*dvout, x_min=v_min)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Input amplitude $v_{\rm in}$ [V]', ylab=r'Output amplitude $v_{\rm out}$ [V]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [7, 0]
model = lin

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm', max_iter=3)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Output amplitude $v_{\rm out}$ [V]')
if tix: tick(axf, xmaj=5, ymaj=1)

axr.set_xlabel(r'Input amplitude $v_{\rm in}$ [V]', x=0.8)
if tix: tick(axr, xmaj=0.1, ymaj=1, ymin=0.2)
legend = axf.legend(loc='best')