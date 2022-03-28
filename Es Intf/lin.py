# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:53:55 2021

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions
TEMP = False

# Modello lineare
def lin(x,m,q):
    return -m*x + q


# Linear fit
y=np.array([0.999208793561516,0.998573797135517,0.997950113224512,0.997312815467043,0.996671993864603,0.996022959537613,0.995380874836903,0.994725708040293,0.994099855041785,0.993477462891098,0.992864057400302,0.992224018698006,0.99159993385146,0.990952713457447,0.990282496365352,0.989683150405386,0.989018614010296,0.988383925755408,0.987732374693256,0.987116065139517,0.986485558026735,0.985840937841868,0.985237711552215,0.984622766127021,0.984053612983584])
print(len(y))
x=np.linspace(1,len(y),len(y))
dy=np.array([1.95034E-05,3.76166948446179E-05,5.16152030808066E-05,6.58126748823443E-05,8.00164382491712E-05,0.000109201033627679,0.000123543216210472,0.000138079123742121,0.000151888790957192,0.000165559372514752,0.000178978502961616,0.000192928528623897,0.000206483929585413,0.000220496127025511,0.00025905084010525,0.000272077906469174,0.000286462057415118,0.000300145193689464,0.000289595110296128,0.000302710236227208,0.000316093181747966,0.000329740415636572,0.000342479468801278,0.000339663919758795,0.000351634505455542])
print(len(dy))
dx=np.zeros(len(x))
# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'ordine di diffrazione', ylab=r'sin (theta_m)')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)
# y=y
dy=dy

# linear fit
init = [0.00066, 1]
model = lin


deff = dy
pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init)
m,q=pars
dm,dq=(np.sqrt(covm.diagonal()))
dm=dm/(m**2)
dq=dq/(q**2)
m,q=1/pars
print(m)
print(dm)
print(q,dq)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'sin(theta_m)')
if tix: tick(axf, xmaj=0.1, ymaj=0.2)
if TEMP:
    axt = axf.twinx()
    axt.errorbar(x, temp, 0.001, dx,'b.', ls='',  label='Therm data')
    axt.set_ylabel('Thermistor Voltage $V(TH)$ V')
    axt.axhline(2.69, c='r', alpha=0.5, label='Thermistor Voltage $= 2.69\pm 0.01$ V')
    axt.axhline(2.69 + 1e-3, c='r', ls='--', alpha=0.3); axt.axhline(2.69 - 1e-3, c='r', ls='--', alpha=0.3)


axr.set_xlabel(r'ordine di diffrazione', x=0.8)
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')
plt.show()