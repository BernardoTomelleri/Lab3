import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def sin_func(t, A, nu,phi,B):
    return A*np.sin(2*np.pi*nu*t + phi) + B

file_path = './data/cal/dc-3.4v.txt'
with open(file_path,newline='') as csvfile:
#convert csv removing comments and empty lines
# fieldnames = ['Data']
    csvreader = csv.reader(csvfile)
# reader = csv.DictReader(filter(lambda row: (row[0]!='#' and row[0]!='\n'), csvfile),fieldnames=
# skip_header = next(reader);
# data = list(csvreader);
    n=0;
    decimal_stream = np.array([elem for elem in csvreader]);
    print(decimal_stream.dtype);
    print(decimal_stream.shape[1]);
    bit_stream = np.zeros((decimal_stream.shape[1]-1)*8)
    for ind in range((decimal_stream.shape[1]-1)):
        a = np.binary_repr(int(decimal_stream[0,ind]),width=8);
        b = a[::-1];
        for i in range(8):
            j=ind*8+i;
            bit_stream[j] = a[i];
ind = np.arange(0,bit_stream.shape[0])
plt.scatter(ind,bit_stream)
plt.xlim(200,12000)
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w
bit_stream_mov = moving_average(bit_stream,8)
ind = np.arange(bit_stream_mov.shape[0])
plt.scatter(ind,bit_stream_mov)
plt.xlim(0,2000)
bit_stream_mov1 = moving_average(bit_stream_mov,8)
ind = np.arange(bit_stream_mov1.shape[0])
plt.scatter(ind,bit_stream_mov1)
plt.xlim(0.0,2000)
plt.show()