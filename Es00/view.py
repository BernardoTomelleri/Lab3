# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:57:02 2021

@author: berni
"""
from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres, sine, sqw)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions

t, x_a, x_b = np.genfromtxt('./default.csv', float, delimiter=',',
                            skip_header=13, unpack=True)

t_min = -1; t_max = 1.
# Preliminary plot to visualize the sub-interval of data to analyze
#lab.rc.typeset(usetex=tex, fontsize=12)
fig, (ax1, ax2) = plt.subplots(2, 1)
grid(ax1, xlab='Time [s]', ylab='Channel 1 [V]')
grid(ax2, xlab='Time [s]', ylab='Channel 2 [V]')
ax1.plot(t, x_a, 'y', alpha=0.6); ax2.plot(t, x_b, 'blue', alpha=0.6)

dt = np.full(t.shape, 2e-7); dx = 2e-4*np.ones_like(x_a)
# fit signals
init_a = [np.std(x_a), 1e3, 0., np.mean(x_a)]
init_b = [0.6, 6.667e2, -1, 0, 0.5]
par_bounds = [[0.0, 1], [6e2, 7e2], [0, 7], [-1, 1], [0, 1]]
genetic_pars = lab.gen_init(model=sqw, coords=[t, x_b],
                                bounds=par_bounds, unc=dx)

ax2.plot(t, sqw(t, *init_b), 'grey', alpha=0.6)
for time, pos, mod, init in zip([t, t], [x_a, x_b], [sine, sqw], [init_a, genetic_pars]):
    pars, covm, deff = propfit(mod, time, pos, dt, dx, p0=init, max_iter=0, alg='trf')
    perr, pcor = errcor(covm)
    prnpar(pars, perr, model=mod)
    chisq, ndof, resn, sigma = chitest(mod(time, *pars), pos, unc=deff,
                                         ddof=len(pars), gauss=True, v=True)

    # graphs
    fig, (axf, axr) = pltfitres(mod, time, pos, dt, deff, pars=pars)
    axf.set_ylabel('Signal %c [V]' %('1' if all(pos == x_a) else '2'))
    if tix: lab.tick(axf, xmaj=5, ymaj=50)
    legend = axf.legend(loc='best')

    axr.set_xlabel('Time [s]', x=0.94)
    if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)
plt.show()
