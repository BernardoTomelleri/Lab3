# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:39:19 2021

@author: berni
"""

from phylab import (np, plt, grid, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

''' Variables that control the script '''
tix = False  # manually choose spacing between axis ticks
tex = True  # LaTeX typesetting maths and descriptions

# Modelli di trasferimento
def lpf(f, fT=0):
    return 1./np.sqrt(1+(f/fT)**2)

def ALPF(f, fT, A=1):
    return A/np.sqrt(1+(f/fT)**2)

def hpf(f, fT):
    return 1./np.sqrt(1+(fT/f)**2) 

f, CH1, CH2, phi = np.genfromtxt('./data/bpfnetwork.csv', float, delimiter=',',
                            skip_header=21, unpack=True)

# Input data manipulation
f_min = 100; f_max = 1e6
x, y, dx, dy = lab.mesrange(f, CH2, x_min=f_min, x_max=f_max)
dx = np.full(x.shape, 10); dy = 1e-3*np.abs(y) +1e-3

# Preliminary plot to visualize the sub-interval of data to analyze
lab.rc.typeset(usetex=tex, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab='Frequency $f$ [Hz]', ylab='Phase $\phi(f)$ $[^\circ]$')
ax.errorbar(f, phi, 1e-3*phi, 1e-2*f, 'k.', ls='-', ms=2, alpha=0.8, label='data')
ax.plot(f, (np.arctan(16.06e3/f) + np.arctan(-f/384.))*180/np.pi,
        label=r'$\tan^{-1}\frac{f_2}{f} - \tan^{-1} \frac{f}{f_1}$', zorder=5)
ax.set_xscale('log')
legend = ax.legend(loc='best')
