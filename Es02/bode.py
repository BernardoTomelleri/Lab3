# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:01:39 2021

@author: berni
"""

from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions

# Modelli di trasferimento
def lpf(f, fT):
    return 1./np.sqrt(1+(f/fT)**2) 

def hpf(f, fT):
    return 1./np.sqrt(1+(fT/f)**2) 

f, CH1, CH2, phi = np.genfromtxt('./data/rc1k10nF_new.csv', float, delimiter=',',
                            skip_header=21, unpack=True)

# Input data manipulation
f_min = 100; f_max = 1e6
x, y, dx, dy = lab.mesrange(f, CH2, x_min=f_min, x_max=f_max)
dx = 0.3/(np.log(10)*x); dy = 1e-3*np.abs(y) +1e-3
x = np.log10(x)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Frequency $f$ [Hz]', ylab='Gain $A(f)$')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# gain fit
init = [3.8]
model = lpf
#par_bounds = [[0.0, 1e-6], [0., 0.1], [-1, 1]]
#genetic_pars = lab.gen_init(model, coords=[x, y], bounds=par_bounds, unc=dy)

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm')
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel('Gain $A(f)$')
if tix: lab.tick(axf, xmaj=5, ymaj=50)

axr.set_xlabel('Frequency $f$ [Hz]')
if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)