from scipy.optimize import curve_fit
import numpy as np
from matplotlib import pyplot as plt

f,A1,A2,phi=np.genfromtxt('C:/Users/rossi/OneDrive/Desktop/passabanda.csv', float, delimiter=',',usecols=[0,1,2,3], skip_header=21, unpack=True)
dA2=np.full(shape=len(A2),fill_value=8.7*np.sqrt(2*(0.005**2)))
dA1=np.full(shape=len(A1),fill_value=8.7*np.sqrt(2*(0.005**2)))
def pa(x,fa,A2):
    return 20.*np.log10(A2/np.sqrt(1+(fa/x)**2))
def pb(x,fb,A1):
    return 20.*np.log10(A1/np.sqrt(1+(x/fb)**2))
"""
def banda(x,fb,fa):
    return 20.*np.log10(1./((1981./1984.) + 1./((10.**(pb(x,fb)/20.)) * (10.**(pa(x,fa)/20.)))))
"""
"""
def banda(x,fa,fb,A):
    return 20.*np.log10(A*((10.**(pb(x,fb,1)/20.)) * (10.**(pa(x,fa,1)/20.))))
"""
def banda(x,fa,fb,c):
    return 20.*np.log10(1./(np.sqrt((c+fa/fb + 1)**2+(x/fb - fa/x)**2)))
fig= plt.figure("Passa banda")
fig.add_axes((.1,.3,.8,.6))

plt.xscale("log")

plt.errorbar(f,A2,dA2,label="out signal data & error",fmt=".")
plt.errorbar(f,A1,dA1,label="in signal data & error",fmt=".")
plt.ylabel("Guadagno [dB]")

popt,pcov =curve_fit(banda,f,A2,sigma=dA2,p0=np.array([1,1,1]),maxfev=7000)
print("PASSA BANDA")
print(popt)
print(np.sqrt(pcov.diagonal()))
x=np.linspace(0,f.max(),8192)

chisq=(((A2-banda(f,*popt))/dA2)**2.).sum()
plt.plot(f,banda(f,*popt),label="Amplification fit $\chi^2 = %.1f/%d$" % (chisq, len(f)-2))


plt.annotate("Fa= %.2E \u00B1 %.2E [Hz]" %(popt[0],np.sqrt(pcov.diagonal())[0]),(10000,-6))

plt.annotate("Fb= %.2E \u00B1 %.2E [Hz]" %(popt[1],np.sqrt(pcov.diagonal())[1]),(700,-6))

plt.annotate("A= %.2E \u00B1 %.2E [Hz]" %(popt[2],np.sqrt(pcov.diagonal())[2]),(700,-8))

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
plt.annotate("Fb= %.2E \u00B1 %.2E [Hz]" %(popt[0],np.sqrt(pcov.diagonal())[0]),(700,-5))

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
print("PASSA ALTO")
popt,pcov =curve_fit(pa,f,A2,sigma=dA2,maxfev=7000)
print(popt)
print(np.sqrt(pcov.diagonal()))
x=np.linspace(0,f.max(),8192)

chisq=(((A2-pa(f,*popt))/dA2)**2.).sum()
plt.plot(f,pa(f,*popt),label="Amplification fit $\chi^2 = %.1f/%d$" % (chisq, len(f)-2))
plt.annotate("Fa= %.2E \u00B1 %.2E [Hz]" %(popt[0],np.sqrt(pcov.diagonal())[0]),(800,-5))

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

f,A1,A2,phi=np.genfromtxt('C:/Users/rossi/OneDrive/Desktop/passabanda.csv', float, delimiter=',',usecols=[0,1,2,3], skip_header=21, unpack=True)
dA2=np.full(shape=len(A2),fill_value=8.7*np.sqrt(2*(0.005**2)))
dA1=np.full(shape=len(A1),fill_value=8.7*np.sqrt(2*(0.005**2)))
def retta(x,m,q):
    return 20*np.log10(x*m + q)

fig= plt.figure("Passa Banda plot di Bode")
fig.add_axes((.1,.3,.8,.6))

plt.xscale("log")

plt.errorbar(f,A2,dA2,label="out signal data & error",fmt=".")
plt.errorbar(f,A1,dA1,label="in signal data & error",fmt=".")
plt.ylabel("Guadagno [dB]")

popt1,pcov1 =curve_fit(retta,f[0:100],A2[0:100],sigma=dA2[0:100],maxfev=7000)
popt2,pcov2 =curve_fit(retta,f[250:450],A2[250:450],sigma=dA2[250:450],maxfev=7000)
popt1,pcov1 =curve_fit(retta,f[0:100],A2[0:100],sigma=dA2[0:100],maxfev=7000)
print("BODE PASSA BANDA")
print(popt1)
print(np.sqrt(pcov1.diagonal()))
x=np.linspace(0,f.max(),8192)

chisq=(((A2[0:100]-retta(f[0:100],*popt1))/dA2[0:100])**2.).sum()
plt.plot(f[0:300],retta(f[0:300],*popt1),color="black",label="Amplification fit $\chi^2 = %.1f/%d$" % (chisq, len(f)-2))
plt.plot(f[0:600],retta(f[0:600],*popt2),color="black",label="Amplification fit $\chi^2 = %.1f/%d$" % (chisq, len(f)-2))

plt.legend()
fig.add_axes((.1,.05,.8,.2))
plt.ylabel("residuals norm.")
plt.xlabel("frequenza [Hz]")

plt.xscale("log")
plt.grid(which="both", color="gray",ls="dashed")
res=(A2[0:100]-retta(f[0:100],*popt1))/dA2[0:100]
print("\n")

covar=np.array(pcov1, copy=1)
for i in range(np.size(covar,0)):
    for j in range(np.size(covar,1)):
        covar[i][j]/=np.sqrt(pcov1.diagonal())[j]*np.sqrt(pcov1.diagonal())[i]
plt.errorbar(f[0:100],res,color="black")
print(chisq)
print("\n")
print(covar)
print("\n\n\n\n")
plt.show()




