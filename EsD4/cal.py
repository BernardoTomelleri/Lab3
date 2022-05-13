# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:25:31 2022

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Modello lineare
def lin(x, m=1, q=0):
    return m*x + q

vin, dvin, vout, dvout = np.loadtxt('./data/cal.txt', float, unpack=True)
v_min = -5; v_max = 5

# Linear fit
x, y, dx, dy = mesrange(vin, vout, dx=dvin, dy=dvout,
                        x_min=v_min, x_max=v_max)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Input amplitude $v_{\rm in}$ [V]', ylab=r'Output amplitude $v_{\rm out}$ [V]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [0.5, 0.5]
model = lin

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm', max_iter=1, tail=2)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fitfig, (axf, axr) = plt.subplots(**lab.rc.PLOT_FIT_RESIDUALS)
grid(axf, xlab=False); grid(axr, ylab='residuals')

axf.errorbar(x, y, dy, dx, marker='.', ms=3, color='k', elinewidth=1, capsize=1.5, ls='', label='data')
axf.plot(x, model(x, *pars), ls='-', marker=None, color='red', label=r'linear fit $\chi^2 = %.1f/%d$' % (chisq, ndof), zorder=10)

axr.errorbar(x, resn, None, None, marker='o', ms=2, elinewidth=0.5, capsize=0.5,
             ls='--', lw=1, color='k')
axr.axhline(0, **lab.rc.RES_HLINE)

axf.set_ylabel('Reconstructed signal [ADC counts]' )
axr.set_xlabel(r'Input Voltage $v_{\rm in}$ [V]', x=0.8)
legend = axf.legend(loc='best')
