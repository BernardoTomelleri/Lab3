# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:05:45 2021

@author: berni
"""

from lab import (np, plt, grid, tick, mesrange, propfit, curve_fit, errcor, prnpar, chitest, pltfitres)
import rc

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Modelli di trasferimento e lineare
def lin(x, m=1, q=0):
    return m*x + q


f, CH1, CH2, phi = np.genfromtxt('./data/rc2k10nF_new.csv', float, delimiter=',',
                            skip_header=21, unpack=True)

f_lo = 500; f_hi = 4e4

# Linear fit to high frequency values
x, y, dx, dy = mesrange(f, CH2, x_min=f_hi)
dx = 0.3/(np.log(10)*x); dy = 1e-3*np.abs(y) +1e-3
x = np.log10(x)

# Preliminary plot to visualize the sub-interval of data to analyze
rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Frequency $f$ [Hz]', ylab='Gain $A(f)$')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [-20, 1]
model = lin
#par_bounds = [[0.0, 1e-6], [0., 0.1], [-1, 1]]
#genetic_pars = lab.gen_init(model, coords=[x, y], bounds=par_bounds, unc=dy)

pars, covm, deff = propfit(model, x, y, dx, dy, p0=init, alg='lm')
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
space = np.linspace(3.7, 6.2, 5000)
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars, space=space)
axf.set_ylabel('Gain $A(f)$ [dB]')
if tix: tick(axf, xmaj=5, ymaj=50)

axr.set_xlabel('Frequency $\log_{10}(f)$ [Hz]', x=0.8)
if tix: tick(axr, xmaj=5, ymaj=2, ymin=0.5)

# Constant fit for low frequency data
def const(x, c=0):
    return c

xl, yl, dxl, dyl = mesrange(f, CH2, x_min=0, x_max=f_lo)
dxl = 0.3/(np.log(10)*xl); dyl = 1e-2*np.abs(yl) +1e-2
xl = np.log10(xl)

popt, pcov = curve_fit(const, xl, yl, sigma=dyl)
errs, corm = errcor(pcov)
prnpar(popt, errs, const)
chisq, ndof, resn = chitest(const(xl, *popt), yl, unc=dyl, ddof=len(popt), v=True)

space = np.linspace(1.9, 4, 5000)
fit = np.full(space.shape, popt[0])
axf.errorbar(xl, yl, dyl, dxl, 'k.', ls='', ms=2, alpha=0.8)
axr.errorbar(xl, resn, None, None, **rc.NORMRES_MARKER)
axf.plot(space, fit, label=r'costant fit $\chi^2 = %.f/%d$' % (chisq, ndof))
axf.errorbar(np.log10(f), CH2, 1e-3*np.abs(CH2) +1e-3, 0.3/(np.log(10)*f), 'g.', ls='',
             ms=2, alpha=0.05, zorder=0)
legend = axf.legend(loc='best')

#fc = space[np.argmin(np.abs(popt[0] - lin(space, *pars)))]
a, b = pars; da, db = perr
c = popt[0]; dc = errs[0]
fc = (c - b)/a
dfc = np.sqrt((((c - a)/(a**2))*da)**2 + (db/a)**2 +(dc/a)**2 - 2*covm[0][1]*(1/a)**2)
print('Corner frequency: %f +- %f Hz'  % (10**fc, np.log(10)*dfc*10**fc))