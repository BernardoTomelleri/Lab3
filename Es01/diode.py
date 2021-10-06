# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 04:11:04 2021

@author: berni
"""
from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions

# Legge di Shockley
def sck(V, Is, VT):
    return Is*(np.exp(V/VT) - 1.)

V, I = np.genfromtxt('./data/shockley.csv', float, delimiter=',',
                            skip_header=6, unpack=True)

V_min = 0; V_max = 3
x, y, dx, dy = lab.mesrange(V, I, x_min=V_min, x_max=V_max)
y*=1e3
dx = np.full(x.shape, 1e-3); dy = 1e-2*y +1e-3

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Differenza di Potenziale $\Delta V$ [V]', ylab='Intensità di Corrente $I$ [mA]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# fit diode I-V curve with Shockley's law
init = [1e-2, 0.3]
par_bounds = [[0., 0.1], [0., 2]]
genetic_pars = lab.gen_init(model=sck, coords=[x, y], bounds=par_bounds, unc=dy)

ax.plot(x, sck(x, *init), 'grey', alpha=0.6)

pars, covm, deff = propfit(sck, x, y, dx, dy, p0=init, alg='lm')
perr, pcor = errcor(covm)
prnpar(pars, perr, model=sck)
chisq, ndof, resn, sigma = chitest(sck(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# fit graphs
fig, (axf, axr) = pltfitres(sck, x, y, dx, deff, pars=pars)
axf.set_ylabel('Intensità di Corrente $I$ [mA]')
if tix: lab.tick(axf, xmaj=5, ymaj=50)
legend = axf.legend(loc='best')

axr.set_xlabel('Differenza di Potenziale $\Delta V$ [V]')
if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)
