# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 04:11:04 2021

@author: berni
"""
from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres, logistic)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Legge di Shockley
def sck(V, Is, VT, ofs=0):
    return Is*(np.exp(V/VT) - 1.) + ofs

def log(x, L=1, k=1, x0=0, ofs=0):
    return logistic(x, L, k, x0) + ofs

V, I = np.genfromtxt('./data/shockley.csv', float, delimiter=',',
                            skip_header=6, unpack=True)

V_min = 0; V_max = 3
x, y, dx, dy = lab.mesrange(V, I, x_min=V_min, x_max=V_max)
y*=1e3
dx = np.full(x.shape, 1e-3); dy = 2e-2*y +2e-2

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Differenza di Potenziale $\Delta V$ [V]', ylab='Intensità di Corrente $I$ [mA]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# fit diode I-V curve with Shockley's law
init = [1.19942817e+01,  2.00000000e+01,  1.92426531e+00, -1.02660255e-02]
model = log
par_bounds = [[0.0, 1000], [0., 30.], [-20, 20], [-1, 1]]
genetic_pars = lab.gen_init(model, coords=[x, y], bounds=par_bounds, unc=dy)

ax.plot(x, model(x, *init), 'grey', alpha=0.6)
pars = genetic_pars

#pars, covm, deff = propfit(model, x, y, dx, dy, p0=genetic_pars, alg='lm')
#perr, pcor = errcor(covm)
#prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=dy, ddof=len(pars), v=True)

# fit graphs
xx = np.linspace(start=-5e-2, stop=np.max(x) + 1e-2, num=2000)
fig, (axf, axr) = pltfitres(model, x, y, dx, dy, pars=pars)
axf.plot(xx, model(xx, *pars), ls='-',
         label=r'logistic fit $\chi^2 = %.1f/%d$' % (chisq, ndof))
axf.set_ylabel('Intensità di Corrente $I$ [mA]')
if tix: lab.tick(axf, xmaj=5, ymaj=50)
legend = axf.legend(loc='best')

axr.set_xlabel('Differenza di Potenziale $\Delta V$ [V]')
if tix: lab.tick(axr, xmaj=5, ymaj=2, ymin=0.5)
