# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:58:45 2022

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

V, I = np.genfromtxt('./data/dark.csv',  float, delimiter=',',
                     skip_header=1, usecols=(0,1), unpack = True)
V_min = 0.1; V_max = 2
dV = np.sqrt((V*5e-3)**2 + (25e-3/np.sqrt(12))**2)
dI = np.sqrt((4e-3*I)**2 + (5e-3*I)**2 + (20e-3/np.sqrt(12))**2)
I*=1e3; dI*=1e3

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

# re save dark currents for later use
xD, yD, dxD, dyD = x, y, dx, dy 

# Power step model
b, I0 = pars
def inp(V, a, V0, alpha):
    # return np.heaviside(V0 - V, 0)*a*(V0 - V)**alpha  + b*V + I0
    return np.piecewise(V, [V < V0, V > V0], [lambda V: a*(V0 - V)**alpha, lambda V: b*V + I0])
def IV(V, a, V0, alpha, b, I0):
    return np.piecewise(V, [V < V0, V > V0], [lambda V: a*(V0 - V)**alpha, lambda V: b*V + I0])

V, I = np.genfromtxt('./data/450nm.csv',  float, delimiter=',',
                     skip_header=1, usecols=(0,1), unpack = True)

V_min = 0.02; V_max = 2
dV = np.sqrt((V*5e-3)**2 + (25e-3/np.sqrt(12))**2)
dI = np.sqrt((4e-3*I)**2 + (5e-3*I)**2 + (20e-3/np.sqrt(12))**2)
I*=1e3; dI*=1e3

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
pars, covm = lab.curve_fit(model, x, y, sigma=deff, p0=init, absolute_sigma=False, method='trf')
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

data = np.column_stack([
    *np.genfromtxt('./data/450nm.csv',  float, delimiter=',',
                     skip_header=6, unpack=True),
    *np.genfromtxt('./data/499nm.csv',  float, delimiter=',',
                         skip_header=6, unpack=True),
    *np.genfromtxt('./data/546nm.csv',  float, delimiter=',',
                         skip_header=6, unpack=True),
    *np.genfromtxt('./data/577nm.csv',  float, delimiter=',',
                         skip_header=6, unpack=True)
]).T

Vs = data[0::2]; Is =data[1::2]

fig, (axf, axr) = plt.subplots(**lab.rc.PLOT_FIT_RESIDUALS)
grid(axf, xlab=False); grid(axr)
lambdas = ['450 nm', '499 nm', '546 nm', '577 nm']
colours = ['blueviolet', 'aquamarine', 'lime', 'yellow']
V0s = []; dV0s = []  
for V, I, l, c  in zip(Vs, Is, lambdas, colours):
    # subset of data extraction
    dV = np.sqrt((V*5e-3)**2 + (25e-3/np.sqrt(12))**2)
    dI = np.sqrt((4e-3*I)**2 + (5e-3*I)**2 + (20e-3/np.sqrt(12))**2)
    I*=1e3; dI*=1e3
    x, y, dx, dy = mesrange(V, I, dx=dV, dy=dI,
                        x_min=V_min, x_max=V_max)
    pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init, absolute_sigma=False, method='trf')
    perr, pcor = errcor(covm)
    prnpar(pars, perr, model)
    chisq, ndof, resn = chitest(model(x, *pars), y, unc=dy, ddof=len(pars), v=True)

    # power law fit graphs
    axf.errorbar(x, y, dy, dx, marker='.', ms=3, color=c,
            elinewidth=1., capsize=1.5, ls='', label=l)
    axf.plot(np.sort(x), model(np.sort(x), *pars), ls='-',
             marker=None, label=r'%s fit $\chi^2 = %.f/%d$' % (l, chisq, ndof), zorder=10)
    #axf.axvline(pars[1], ls='-.', label='V0')
    
    axr.errorbar(x, resn, None, None, marker='o', ms=2, elinewidth=0.5, capsize=0.5,
                 ls='--', lw=1, color=c)
    V0s.append(pars[1]); dV0s.append(perr[1])
    
axf.errorbar(xD, yD, dyD, dxD, marker='.', ms=3, color='k',
        elinewidth=1., capsize=1.5, ls='', label=r'dark current $I_0$', zorder=0)
axr.axhline(0, **lab.rc.RES_HLINE)

axf.set_ylabel(r'Photocurrent intensity $I(V)$ [pA]')
if tix: tick(axf, xmaj=0.1, ymaj=50)

axr.set_xlabel(r'Bias voltage $V$ [V]', x=0.8)
axr.set_ylabel(r'norm. residuals ')
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')

#linear fit for h/e ratio
x = np.array([.668, .601, .549, .520])
dx = np.array([9.6, 11.7, 11.1, 10.])/np.array([450, 499, 546, 577]) * x/2.
y, dy = V0s, dV0s

# linear fit
init = [4, 0]
model = lin

pars, covm, deff = propfit(model, x, y, dy=dy, p0=init)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Stopping voltage $V_0$ [V]')
if tix: tick(axf, xmaj=0.1, ymaj=50)

axr.set_xlabel(r'Light frequency $\nu$ [PHz]', x=0.7)
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')