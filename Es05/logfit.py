# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:04:00 2021

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Modello logaritmico
def log(x, a=1, b=0):
    return a*np.log(x) + b

vin, dvin, vout, dvout = np.loadtxt('./data/TOT.txt', float, unpack=True)
vin*=2e-3; dvin*=2e-3
v_min = 0; v_max = 3

# Linear fit
x, y, dx, dy = mesrange(vin, vout, dx=dvin, dy=dvout,
                        x_min=v_min, x_max=v_max)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Input charge $Q_{\rm in}$ [nC]', ylab=r'Time-over-Threshold [$\mu$s]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# logarithmic fit
init = [1, 1]
model = log

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm', max_iter=3, tail=2)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# log fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Time-over-Threshold [$\mu$s]')
if tix: tick(axf, xmaj=5, ymaj=0.05)

axr.set_xlabel(r'Input charge $Q_{\rm in}$ [nC]', x=0.8)
if tix: tick(axr, xmaj=0.05, ymaj=0.1, ymin=0.02)
legend = axf.legend(loc='best')
