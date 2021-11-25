# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:58:58 2021

@author: berni
"""
from phylab import (np, plt, grid, errcor, prnpar, chitest, propfit, pltfitres, tick)
import phylab as lab

''' Variables that control the script '''
tex = True # LaTeX typesetting maths and descriptions
tix = True  # manually choose spacing between axis ticks

# Modello esponenziale
def exp(x, a=1, b=1):
    return a*np.exp(-x/b)

t, V = np.genfromtxt('./data/vshaper.csv', float, delimiter=',', 
                                 skip_header=6, unpack=True)
t_min = 2e-6; t_max = 1e3
x, y, t_b, x_b = lab.mesrange(t, V, x_min=t_min, x_max=t_max)
x *= 1e6

fig, ax = plt.subplots()
ax.plot(t*1e6, V, 'gray')

dx, dy = 1e-3*x, 1e-3*y + 5e-3
# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
grid(ax, xlab=r'Time $t$ [$\mu$s]', ylab=r'$V_{sh}(t)$ [V]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# exp decay fit
init = [1, 1]
model = exp

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm', max_iter=3, tail=2)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'$V_{sh}(t)$ [V]')
if tix: tick(axf, xmaj=5, ymaj=0.2)

axr.set_xlabel(r'Time $t$ [$\mu$s]', x=0.8)
if tix: tick(axr, xmaj=100, ymaj=2)
legend = axf.legend(loc='best')
