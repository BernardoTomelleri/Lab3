import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def sin_func(t, A, nu,phi,B):
    return A*np.sin(2*np.pi*nu*t + phi) + B

file_path = "C:/Users/rossi/OneDrive/Documenti/GitHub/Lab3/EsD4/data/freq/5khz.txt"
with open(file_path,newline='') as csvfile:
#convert csv removing comments and empty lines
# fieldnames = ['Data']
    csvreader = csv.reader(csvfile)
# reader = csv.DictReader(filter(lambda row: (row[0]!='#' and row[0]!='\n'), csvfile),fieldnames=
# skip_header = next(reader);
# data = list(csvreader);
    n=0;
    decimal_stream = np.array([elem for elem in csvreader]);
    bit_stream = np.zeros((decimal_stream.shape[1]-1)*8)
    for ind in range((decimal_stream.shape[1]-1)):
        a = np.binary_repr(int(decimal_stream[0,ind]),width=8);
        b = a[::-1];
        for i in range(8):
            j=ind*8+i;
            bit_stream[j] = a[i];
ind = np.arange(0,bit_stream.shape[0])
bit_stream=np.abs(1-bit_stream)
plt.subplot(2,1,1)
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w
bit_stream_mov = moving_average(bit_stream,8)
ind = np.arange(bit_stream_mov.shape[0])
bit_stream_mov1 = moving_average(bit_stream_mov,8)
ind = np.arange(bit_stream_mov1.shape[0])


plt.errorbar(ind,bit_stream_mov1,linestyle="none",fmt=".")
plt.grid()
plt.xlim(0.0,2000)

sigma=np.full_like(ind,1./255.,dtype=float)
popt,pcov=optimize.curve_fit(sin_func,ind,bit_stream_mov1,p0=np.array([1,0.09,1,0]))
z=np.linspace(ind[0],2000,30000)
plt.plot(z,sin_func(z,*popt))
res=bit_stream_mov1-sin_func(ind,*popt)
print(len(res))
chisq=((res/1.)**2.).sum()
print("chisq",chisq)
plt.subplot(2,1,2)
plt.errorbar(ind,res)
plt.xlim(0.0,2000)
plt.grid()
print("A = ", + popt[0],"+-",np.sqrt(pcov.diagonal())[0])
print("nu = ", + 50000.*popt[1],"+-",50000*np.sqrt(pcov.diagonal())[1])
print("phi = ", + popt[2],"+-",np.sqrt(pcov.diagonal())[2])
print("B = ", + popt[3],"+-",np.sqrt(pcov.diagonal())[3])

noise=np.var(res)
AMP=(popt[0]/np.sqrt(2))**2.
SNR=20*np.log10(AMP/noise)
print(SNR)
freq=np.array([100,200,500,1000,2000,5000,10000])
A=np.array([0.38688,0.3857557,0.3796857,0.356494,0.27784,0.02298,0.019])/A[0]
dA=np.array([0.00022,0.000216,0.000223,0.0000867,0.0000811,0.0000814,0.0000795])
plt.figure()
plt.errorbar(freq,A,dA,linestyle="none",fmt="o",color="orange")
plt.xscale("log")
plt.xlabel("frequenza [Hz]")
plt.ylabel("ampiezza relativa ricostruita [u.a.]")
plt.grid()
plt.axhline(1,linestyle="--",color="black")
plt.show()