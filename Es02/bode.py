# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:05:45 2021

@author: berni
"""

from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions

# Modelli di trasferimento e lineare
def lin(x, m=1, q=0):
    return m*x + q

def hpf(f, fT):
    return 1./np.sqrt(1+(f/fT)**2) 

def lpf(f, fT):
    return 1./np.sqrt(1+(fT/f)**2) 

f, G = np.genfromtxt('./data/trgdiode10Hz1Vamp.csv', float, delimiter=',',
                            skip_header=6, unpack=True)

f_min = 0; f_max = 1.76
x, y, dx, dy = lab.mesrange(f, G, x_min=f_min, x_max=f_max)

dx = np.full(x.shape, 1e-3); dy = 1e-3*np.abs(y) +1e-3

# Preliminary plot to visualize the sub-interval of data to analyze
#lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Frequency $f$ [Hz]', ylab='Gain $A(f)$')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [1e-6, 0.056, -2e-2]
model = lin
par_bounds = [[0.0, 1e-6], [0., 0.1], [-1, 1]]
genetic_pars = lab.gen_init(model, coords=[x, y], bounds=par_bounds, unc=dy)

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm')
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel('Gain $A(f)$')
if tix: lab.tick(axf, xmaj=5, ymaj=50)
legend = axf.legend(loc='best')

axr.set_xlabel('Frequency $f$ [Hz]')
if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)
