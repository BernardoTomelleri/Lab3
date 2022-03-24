from scipy.optimize import curve_fit
import numpy as np
from matplotlib import pyplot as plt
def fun(x,m,q):
    return m*x+q

R=np.array([4.4,4.7,5.0,5.2,5.4,5.7,5.9,6.1])/100-0.002
dR=np.array([0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3])/100
B=0.00074101*1.40
dB=0.02*0.00074101
Vacc=np.array([150,170,190,210,230,250,270,290])
dVacc=np.array([1,1,1,1,1,1,1,1])
rap=2*Vacc/((R*B)**2)
drap=np.sqrt((dR*(4*Vacc*R*B*B/((R*R*B*B)**2)))**2 + (dB*(4*Vacc*R*R*B/((R*R*B*B)**2)))**2+ (2*dVacc*R*R*B*B/((R*R*B*B)**2))**2)
em=((1./(drap**2))*rap).sum()/((1./(drap**2)).sum())
dem=1./(np.sqrt((1./(drap**2)).sum()))
print(em)
print(dem)
plt.subplot(2,1,1)
plt.errorbar(Vacc,rap,drap,dVacc,linestyle="none",color="orange")
plt.grid()
plt.xlabel("Vacc [V]")
plt.ylabel("e/m [C/Kg]")
plt.axhline(em,ls="--",color="black")
plt.subplot(2,1,2)
plt.errorbar(Vacc,(rap-em)/drap,linestyle="--",color="black")
plt.xlabel("Vacc [V]")
plt.ylabel("norm. res.")
plt.grid()
plt.axhline(0)
plt.show()