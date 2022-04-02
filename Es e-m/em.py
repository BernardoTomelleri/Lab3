from scipy.optimize import curve_fit
import numpy as np
from matplotlib import pyplot as plt

from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

T=np.array([0.00131711711711712,0.00137297297297297,0.00141621621621622,0.00144324324324324,0.00145585585585586,0.00146486486486487,0.00146666666666667,0.00147027027027027,0.00147207207207207,0.00147027027027027,0.00147387387387387,0.00147207207207207,0.00147027027027027,0.00147207207207207,0.00147207207207207,0.00146846846846847,0.00146486486486487,0.00145225225225225,0.00143423423423423,0.00140720720720721,0.00134774774774775,0.00125225225225225])
d=np.linspace(-10,11,22)/100
dT=np.array([2.88915049263828E-05,3.01167260655317E-05,3.10652843668083E-05,3.16581333051062E-05,3.19347961429785E-05,3.21324124557445E-05,3.21719357182977E-05,0.000032250982243404,3.22905055059572E-05,0.000032250982243404,3.23300287685104E-05,3.22905055059572E-05,0.000032250982243404,3.22905055059572E-05,3.22905055059572E-05,3.22114589808509E-05,3.21324124557445E-05,3.18557496178721E-05,3.14605169923402E-05,3.08676680540424E-05,0.000029563400389787,2.74686674744679E-05])
dd=np.full_like(d,0.1)/100
dT=np.sqrt((-T*(np.max(dT)**2)/(np.max(T)**2))**2 + (dT/np.max(T))**2)
T=T/np.max(T)
d=np.abs(d)
#dT = np.array([dT, np.abs(T - np.max(T))])
plt.errorbar(d,T,dT,dd, marker='.', ms=3, elinewidth=1., capsize=1.5)
grid(plt.gca())
plt.xlabel("Distanza dal centro [m]")
plt.ylabel("Campo magnetico $B/B_{MAX}$ [T]")
plt.show()