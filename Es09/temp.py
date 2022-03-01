# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:07:29 2022

@author: berni
"""

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = False  # LaTeX typesetting maths and descriptions
TEMP= False
# Modello lineare
def velt(x, v0):
    return v0*np.sqrt((x+273.15)/(273.15))

def therm(R):
    return 1/(1./T_0 + (np.log(R/R_0))/B)

time, Vtemp = np.genfromtxt('C:/Users/rossi/OneDrive/Documenti/GitHub/Lab3/Es09/data/temptime.csv',  float, delimiter=',',
                     skip_header=1, usecols=(0,1), unpack = True)
t_min = 0; t_max = 300
R=9950
B=3950
T_0=298.15
R_0=10000
dR=80
M=4.99
dM=0.03
s=252
ds=1
vel=2*s/time
dtime=time*0.001
dv=np.sqrt((2*ds/time)**2 + (2*s*dtime/(time**2))**2)
T=Vtemp*R/(M-Vtemp)
dVtemp=Vtemp*0.005
dT=np.sqrt(((Vtemp/(M-Vtemp))*dR)**2 + ((Vtemp*R/((M-Vtemp)**2))*dM)**2 + ((R*M/((M-Vtemp)**2))*dVtemp)**2)

dT=dT*(1/R_0/(T/R_0)/B)*(1/T_0 + np.log(T/R_0)/B)**(-2)
T=therm(T)
print(T)
print(dT)
# Linear fit

T=T-273.15
x, y, dx, dy = mesrange(T,vel, dx=dT, dy=dv,
                        x_min=t_min, x_max=t_max)


# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Temperature [Celsius]', ylab=r'travel distance $s(t)$ [mm]')
ax.errorbar(x, y, dy, dx, 'k.', ls='-', ms=2, alpha=0.8)

# linear fit
init = [331]
model = velt

deff = dy
pars, covm = lab.curve_fit(model, x, y, sigma=dy, p0=init)
perr, pcor = errcor(covm)
prnpar(pars, perr, model)
chisq, ndof, resn = chitest(model(x, *pars), y, unc=deff, ddof=len(pars), v=True)

# linear fit graphs
fig, (axf, axr) = pltfitres(model, x, y, dx, deff, pars=pars)
axf.set_ylabel(r'Speed of sound [m/s]')
if tix: tick(axf, xmaj=0.1, ymaj=0.2)
if TEMP:
    axt = axf.twinx()
    axt.errorbar(x, temp, 0.001, dx,'b.', ls='',  label='Therm data')
    axt.set_ylabel('Thermistor Voltage $V(TH)$ V')
    axt.axhline(2.69, c='r', alpha=0.5, label='Thermistor Voltage $= 2.69\pm 0.01$ V')
    axt.axhline(2.69 + 1e-3, c='r', ls='--', alpha=0.3); axt.axhline(2.69 - 1e-3, c='r', ls='--', alpha=0.3)


axr.set_xlabel(r'Temperature [Celsius]', x=0.8)
if tix: tick(axr, xmaj=0.1, ymaj=0.5)
legend = axf.legend(loc='best')
plt.show()