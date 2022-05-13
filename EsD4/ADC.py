import csv
from phylab import (np, plt, grid, tick, mesrange, propfit, errcor, prnpar, chitest, pltfitres)
import phylab as lab

def sin_func(t, A, nu,phi,B):
    return A*np.sin(2*np.pi*nu*t + phi) + B

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

file_path = "./data/freq/2khz.txt"
with open(file_path,newline='') as csvfile:
#convert csv removing comments and empty lines
# fieldnames = ['Data']
    csvreader = csv.reader(csvfile)
# reader = csv.DictReader(filter(lambda row: (row[0]!='#' and row[0]!='\n'), csvfile),fieldnames=
# skip_header = next(reader);
# data = list(csvreader);
    n=8;
    decimal_stream = np.array([elem for elem in csvreader][0]).astype(np.uint8)
    bit_stream = np.unpackbits(decimal_stream)
            
# sampling interval in ms
t_samp = 20e-3
ind = np.arange(len(bit_stream))
t_min = 0.; t_max=5

# moving average graphs
lab.rc.typeset(usetex=True, fontsize=12)
fig, ax = plt.subplots()
grid(ax, xlab=r'Time $t$ [ms]', ylab=r'Reconstructed signal [ADC counts]')
x, y, dx, dy = mesrange(ind*t_samp, bit_stream, dx=np.full_like(ind, 1e-6),
                        dy=np.full_like(ind, 1./255), x_min=t_min, x_max=t_max)
ax.errorbar(x, y, marker='.', ls=' ', label='bit stream')

mov_avg1 = moving_average(y, n)
ind = np.arange(len(mov_avg1)); x = ind*t_samp
ax.errorbar(x, mov_avg1, marker='.', ls=' ', label='first moving average')

mov_avg2 = moving_average(mov_avg1, n)
ind = np.arange(len(mov_avg2)); x = ind*t_samp
x = x[::n-1]; mov_avg2 = mov_avg2[::n-1]
ax.errorbar(x, mov_avg2, marker='.',  label='decimated second moving average')
legend = ax.legend(loc='upper right')

# sinusoidal fit
dx=np.full_like(x, 1e-6); dy=np.full_like(x, 3./255)
popt, pcov = lab.curve_fit(sin_func, x, mov_avg2, p0=np.array([1, 2, 1,1]))
res=(mov_avg2 - sin_func(x, *popt))/(255./255.)

perr, pcor = errcor(pcov)
prnpar(popt, perr, model=sin_func)
chisq, ndof, resn, sigma = chitest(sin_func(x, *popt), mov_avg2, unc=dy,
                                     ddof=len(popt), gauss=True, v=True)

# fit graphs
fitfig, (axf, axr) = plt.subplots(**lab.rc.PLOT_FIT_RESIDUALS)
grid(axf, xlab=False); grid(axr, ylab='residuals')
xx = np.linspace(np.min(0.9*x), np.max(1.05*x), 2000)

axf.errorbar(x, mov_avg2, dy, dx, marker='.', ms=3, color='k', elinewidth=.5, capsize=1.5, ls='', label='data')
axf.plot(xx, sin_func(xx, *popt), ls='-', marker=None, color='red', label=r'sine fit $\chi^2 = %.f/%d$' % (chisq, ndof), zorder=10)

axr.errorbar(x, res, None, None, marker='o', ms=2, elinewidth=0.5, capsize=0.5,
             ls='--', lw=1, color='k')
axr.axhline(0, **lab.rc.RES_HLINE)

axf.set_ylabel('Reconstructed signal [ADC counts]' )
axr.set_xlabel('Time [s]', x=0.9)
legend = axf.legend(loc='best')

noise=np.var(res)
AMP=(popt[0]/np.sqrt(2))**2.
SNR=20*np.log10(AMP/noise)
print(SNR)
freq=np.array([100,200,500,1000,2000,5000,10000])
A=np.array([0.38688,0.3857557,0.3796857,0.356494,0.27784,0.02298,0.019])
Adb = 20*np.log10(A/A[0])
dA = np.array([0.00022,0.000216,0.000223,0.0000867,0.0000811,0.0000814,0.0000795])
dA = 8.7 * dA/A 
frqfig, ax = plt.subplots()
grid(ax, xlab=r'Frequency $f$ [Hz]', ylab=r'ADC signal relative amplitude [dB]' )
ax.errorbar(freq, Adb, dA, ls='None', fmt='o', ms=4, color='orange')
ax.set_xscale('log')
#ax.axhline(0,linestyle="--",color="black")
plt.tight_layout()
