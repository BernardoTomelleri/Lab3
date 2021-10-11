# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 04:11:04 2021

@author: berni
"""
from lab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres)
import lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions

# Legge di Shockley
def sck(V, Is, VT, ofs=0):
    return Is*(np.exp(V/VT) - 1.) + ofs

V, I = np.genfromtxt('./data/trgdiode10Hz1Vamp.csv', float, delimiter=',',
                            skip_header=6, unpack=True)

V_min = 0; V_max = 1.76
x, y, dx, dy = lab.mesrange(V, I, x_min=V_min, x_max=V_max)
y*=1e3
dx = np.full(x.shape, 1e-3); dy = 1e-3*np.abs(y) + 1e-3

# Preliminary plot to visualize the sub-interval of data to analyze
#lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Differenza di Potenziale $\Delta V$ [V]', ylab='Intensità di Corrente $I$ [mA]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# fit diode I-V curve with Shockley's law
init = [1e-6, 0.056, -2e-2]
model = sck
par_bounds = [[0.0, 1e-6], [0., 0.1], [-1, 1]]
genetic_pars = lab.gen_init(model, coords=[x, y], bounds=par_bounds, unc=dy)

ax.plot(x, model(x, *genetic_pars), c='grey', alpha=0.6)

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm', chimin=1)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# fit graphs
space = np.linspace(0.95, 1.77, 2000)
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars, space=space)
axf.set_ylabel('Intensità di Corrente $I$ [mA]')
if tix: lab.tick(axf, xmaj=5, ymaj=50)
legend = axf.legend(loc='best')

axr.set_xlabel('Differenza di Potenziale $\Delta V$ [V]')
if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)


# Linear fit for LED equivalent resistance
def lin(x, m=1, q=0):
    return m*x + q

lx, ly, dlx, dly = lab.mesrange(V, I*1e3, x_min=V_max+0.1)
dlx = np.full(lx.shape, 1e-4); dly = 1e-2*ly + 1e-2

popt, pcov = np.polyfit(lx, ly, deg=1, cov=True)
errs, corm = lab.errcor(pcov)
prnpar(popt, errs, model=lin)
chisq, ndof, resn, sigma = chitest(lin(lx, *popt), ly, dly, ddof=len(popt), gauss=True, v=True)

# Linear fit graph
linspace = np.linspace(1.85, 1.91, 2000)
linfig, (axf, axr) = pltfitres(lin, lx, ly, dlx, dly, pars=popt, space=linspace)
axf.set_ylabel('Intensità di Corrente $I$ [mA]')
if tix: lab.tick(axf, xmaj=5, ymaj=50)
legend = axf.legend(loc='best')

axr.set_xlabel('Differenza di Potenziale $\Delta V$ [V]')
if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)
