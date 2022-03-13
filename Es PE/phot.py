# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:58:45 2022

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions

# Modello lineare
def lin(x, m=1, q=0):
    return m*x + q

V, I = np.genfromtxt('./data/dark.csv',  float, delimiter=',',
                     skip_header=1, usecols=(0,1), unpack = True)
V_min = 0.1; V_max = 2
I*=1e3
dV = np.ones_like(V)*0.005; dI = 5e-3*I + 2e-1*np.ones_like(I)

# Linear fit
x, y, dx, dy = mesrange(V, I, dx=dV, dy=dI,
                        x_min=V_min, x_max=V_max)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Bias voltage $V$ [V]', ylab=r'Dark current $I_0$ [pA]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [3, 0]
model = lin

deff = dy
pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init, absolute_sigma=False)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Dark current intensity $I_0$ [pA]')
if tix: tick(axf, xmaj=0.1, ymaj=50)

axr.set_xlabel(r'Bias voltage $V$ [V]', x=0.8)
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')

# Power step model
b, I0 = pars
def inp(V, a, V0, alpha):
    return np.heaviside(V0 - V, 0)*a*(V0 - V)**alpha  + b*V + I0

V, I = np.genfromtxt('./data/499nm.csv',  float, delimiter=',',
                     skip_header=1, usecols=(0,1), unpack = True)

V_min = 0.02; V_max = 1.0
I*=1e3
dV = np.ones_like(V)*0.005; dI = 5e-3*I + 2e-1*np.ones_like(I)

# subset of data extraction
x, y, dx, dy = mesrange(V, I, dx=dV, dy=dI,
                        x_min=V_min, x_max=V_max)

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Bias voltage $V$ [V]', ylab=r'Photocurrent intensity $I(V)$ [pA]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# power law fit
init = [700, 1.09, 2.5]
model = inp

deff = dy
pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init, absolute_sigma=False)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# power law fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Photocurrent intensity $I(V)$ [pA]')
if tix: tick(axf, xmaj=0.1, ymaj=50)

axr.set_xlabel(r'Bias voltage $V$ [V]', x=0.8)
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')