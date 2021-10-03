#!/usr/bin/python3
#Generates 4092 points of a RLC circuit oscillating in response to a square wave
#Results in damped oscillations (alternating in sign) superimposed over square wave.
import math

def getIndex(i, n):
    if i < 0 :
        return n + i
    elif i >= n:
        return i - n
    else :
        return i

#s transform
wn = 6.28*6 #Hz
zeta = 0.3 #damping

#z transform
f = 4092;

#terms
expTerm = math.exp(-zeta*wn/f)
angTerm = wn*math.sqrt(1-zeta*zeta)/f
gainTerm = wn/math.sqrt(1-zeta*zeta)

b0 = 0.
b1 = gainTerm*expTerm*math.sin(angTerm)
b2 = 0
a0 = 1.
a1 = -2*expTerm*math.cos(angTerm)
a2 = expTerm*expTerm

print("a1="+ str(a1))
print("a2="+ str(a2))
print("b1="+ str(b1))


myFile = open('out.dat','w')

origWaveform = []
for i in range(0,round(f/2)):
    origWaveform.append(1.)
for i in range(round(f/2),f):
    origWaveform.append(0.)

newWaveform = []
for i in range(len(origWaveform)):
    newWaveform.append(0.)

for i in range(len(origWaveform)):
    #newWaveform[i] = (1./a0)*(b0*origWaveform[getIndex(i, len(origWaveform))] + b1*origWaveform[getIndex(i-1, len(origWaveform))]+ b2*origWaveform[getIndex(i-2, len(origWaveform))] - a1*newWaveform[getIndex(i-1, len(origWaveform))] - a2*newWaveform[getIndex(i-2, len(origWaveform))])
    newWaveform[i] = b0*origWaveform[getIndex(i, len(origWaveform))] 
    newWaveform[i] += b1*origWaveform[getIndex(i-1, len(origWaveform))]
    newWaveform[i] += b2*origWaveform[getIndex(i-2, len(origWaveform))]
    newWaveform[i] -= a1*newWaveform[getIndex(i-1, len(origWaveform))] 
    newWaveform[i] -= a2*newWaveform[getIndex(i-2, len(origWaveform))]
    newWaveform[i] *= (1./a0)



for val in newWaveform:
    myFile.write(str(val) + "\n")

myFile.close()

