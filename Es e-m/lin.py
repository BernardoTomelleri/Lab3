# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:53:55 2021

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions
TEMP = False

# Modello lineare
def lin(x,m,q):
    return m*x + q

# Linear fit
R=np.array([4.4,4.7,5.0,5.2,5.4,5.7,5.9,6.1])/100-0.002
dR=np.array([0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3])/100
B=0.00074101*1.40
dB=0.02*0.00074101
Vacc=np.array([150,170,190,210,230,250,270,290])
dVacc=np.array([1,1,1,1,1,1,1,1])
rap=2*Vacc/((R*B)**2)
drap=np.sqrt((dR*(4*Vacc*R*B*B/((R*R*B*B)**2)))**2 + (dB*(4*Vacc*R*R*B/((R*R*B*B)**2)))**2+ (2*dVacc*R*R*B*B/((R*R*B*B)**2))**2)
x=(B*R)**2
dx=np.sqrt((2*B*B*R*dR)**2 + (2*B*R*R*dB)**2)
y=2*Vacc
dy=2*dVacc
print(len(dy))
# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'travel time $t$ [ms]', ylab=r'travel distance $s(t)$ [mm]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [3, 0]
model = lin
x, dx, y, dy = y, dy, x, dx
deff = dy
pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init, absolute_sigma=False)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'$(BR)^2$ [T$^2$ m$^2$]')
if tix: tick(axf, xmaj=0.1, ymaj=50)
if TEMP:
    axt = axf.twinx()
    axt.errorbar(x, temp, 0.001, dx,'b.', ls='',  label='Therm data')
    axt.set_ylabel('Thermistor Voltage $V(TH)$ V')
    axt.axhline(2.69, c='r', alpha=0.5, label='Thermistor Voltage $= 2.69\pm 0.01$ V')
    axt.axhline(2.69 + 1e-3, c='r', ls='--', alpha=0.3); axt.axhline(2.69 - 1e-3, c='r', ls='--', alpha=0.3)


axr.set_xlabel(r'$2 V_{\mathrm{acc}}$ [V]', x=0.8)
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')