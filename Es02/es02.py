from scipy.optimize import curve_fit
import numpy as np
from matplotlib import pyplot as plt

f,A1,A2,phi=np.genfromtxt('C:/Users/rossi/OneDrive/Desktop/passabanda.csv', float, delimiter=',',usecols=[0,1,2,3], skip_header=21, unpack=True)
dA2=np.full(shape=len(A2),fill_value=8.7*np.sqrt(2*(0.005**2)))
dA1=np.full(shape=len(A1),fill_value=8.7*np.sqrt(2*(0.005**2)))
def pa(x,fa):
    return 20.*np.log10(1./np.sqrt(1+(fa/x)**2))
def pb(x,fb):
    return 20.*np.log10((1./np.sqrt(1+(x/fb)**2)))
def banda(x,fb,fa):
    return 20.*np.log10(1./((1981./1984.) + 1./((10.**(pb(x,fb)/20.)) * (10.**(pa(x,fa)/20.)))))

fig= plt.figure("Passa banda")
fig.add_axes((.1,.3,.8,.6))

plt.xscale("log")

plt.errorbar(f,A2,dA2,label="out signal data & error",fmt=".")
plt.errorbar(f,A1,dA1,label="in signal data & error",fmt=".")
plt.ylabel("Guadagno [dB]")

popt,pcov =curve_fit(banda,f,A2,sigma=dA2,p0=np.array([16000,380]),maxfev=7000)
print(popt)
print(np.sqrt(pcov.diagonal()))
x=np.linspace(0,f.max(),8192)

chisq=(((A2-banda(f,*popt))/dA2)**2.).sum()
plt.plot(f,banda(f,*popt),label="Amplification fit $\chi^2 = %.1f/%d$" % (chisq, len(f)-2))


plt.annotate("Fa= %.2E \u00B1 %.2E [Hz]" %(popt[0],np.sqrt(pcov.diagonal())[0]),(10000,-6))

plt.annotate("Fb= %.2E \u00B1 %.2E [Hz]" %(popt[1],np.sqrt(pcov.diagonal())[1]),(700,-6))

plt.legend()
fig.add_axes((.1,.05,.8,.2))
plt.ylabel("residuals norm.")
plt.xlabel("frequenza [Hz]")

plt.xscale("log")
plt.grid(which="both", color="gray",ls="dashed")
res=(A2-banda(f,*popt))/dA2
print("\n")

covar=np.array(pcov, copy=1)
for i in range(np.size(covar,0)):
    for j in range(np.size(covar,1)):
        covar[i][j]/=np.sqrt(pcov.diagonal())[j]*np.sqrt(pcov.diagonal())[i]
plt.errorbar(f,res,color="black")
print(chisq)
print("\n")
print(covar)
print("\n\n\n\n")
f,A1,A2,phi=np.genfromtxt('C:/Users/rossi/OneDrive/Desktop/passabasso.csv', float, delimiter=',',usecols=[0,1,2,3], skip_header=21, unpack=True)
dA2=np.full(shape=len(A2),fill_value=8.7*np.sqrt(2*(0.005**2)))
dA1=np.full(shape=len(A1),fill_value=8.7*np.sqrt(2*(0.005**2)))
fig= plt.figure("Passa basso")
fig.add_axes((.1,.3,.8,.6))

plt.xscale("log")

plt.errorbar(f,A2,dA2,label="out signal data & error",fmt=".")
plt.errorbar(f,A1,dA1,label="in signal data & error",fmt=".")
plt.ylabel("Guadagno [dB]")

popt,pcov =curve_fit(pb,f,A2,sigma=dA2,maxfev=7000)
print(popt)
print(np.sqrt(pcov.diagonal()))
x=np.linspace(0,f.max(),8192)

chisq=(((A2-pb(f,*popt))/dA2)**2.).sum()
plt.plot(f,pb(f,*popt),label="Amplification fit $\chi^2 = %.1f/%d$" % (chisq, len(f)-2))
plt.annotate("Fb= %.2E \u00B1 %.2E [Hz]" %(popt,np.sqrt(pcov.diagonal())),(700,0-5))

plt.legend()
fig.add_axes((.1,.05,.8,.2))
plt.ylabel("residuals norm.")
plt.xlabel("frequenza [Hz]")

plt.xscale("log")
plt.grid(which="both", color="gray",ls="dashed")
res=(A2-pb(f,*popt))/dA2

plt.errorbar(f,res,color="black")
print(chisq)
print("\n")
print("\n\n\n")
f,A1,A2,phi=np.genfromtxt('C:/Users/rossi/OneDrive/Desktop/passaalto.csv', float, delimiter=',',usecols=[0,1,2,3], skip_header=21, unpack=True)
dA2=np.full(shape=len(A2),fill_value=8.7*np.sqrt(2*(0.005**2)))
dA1=np.full(shape=len(A1),fill_value=8.7*np.sqrt(2*(0.005**2)))
fig= plt.figure("Passa alto")
fig.add_axes((.1,.3,.8,.6))

plt.xscale("log")

plt.errorbar(f,A2,dA2,label="out signal data & error",fmt=".")
plt.errorbar(f,A1,dA1,label="in signal data & error",fmt=".")
plt.ylabel("Guadagno [dB]")

popt,pcov =curve_fit(pa,f,A2,sigma=dA2,maxfev=7000)
print(popt)
print(np.sqrt(pcov.diagonal()))
x=np.linspace(0,f.max(),8192)

chisq=(((A2-pa(f,*popt))/dA2)**2.).sum()
plt.plot(f,pa(f,*popt),label="Amplification fit $\chi^2 = %.1f/%d$" % (chisq, len(f)-2))
plt.annotate("Fa= %.2E \u00B1 %.2E [Hz]" %(popt,np.sqrt(pcov.diagonal())),(800,-5))

plt.legend()
fig.add_axes((.1,.05,.8,.2))
plt.ylabel("residuals norm.")
plt.xlabel("frequenza [Hz]")

plt.xscale("log")
plt.grid(which="both", color="gray",ls="dashed")
res=(A2-pa(f,*popt))/dA2

plt.errorbar(f,res,color="black")
print(chisq)
print("\n\n\n")
plt.show()




