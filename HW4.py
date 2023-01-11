""" HW4: Fast Fourier Transforms
Sarah Mahl
MATH 3XXX Intro to Numerical Methods
2/8/21 """

import numpy as np
import matplotlib.pyplot as plt
import math

f = open('FourierDataPython.out', 'r')
m = [] # m contains the Fourier coefficients of function m(x), m is already fhats
for line in f:
    m.append(line.strip())
for elem in range(len(m)):
    m[elem] = complex(m[elem])

m_trunc = []
for f in m:
    if f != 0.0:
        m_trunc.append(f)
m_trunc.pop(0)

N = 10
L = 2*np.pi    # x in [-10,10] for #3
x_n = [n*(L/N) for n in range(-N,N)]
fvec = [(6+np.cos(43*x_n[j])+12*np.sin(2*x_n[j])) for j in range(len(x_n))] # g(x) = cos(2x)
fhats = np.fft.fft(fvec)
fourier_transform = np.fft.ifft(fhats) # converts fourier coefficients back to physical space
print(fhats)
real_fourier = np.real(fourier_transform)

x1 = np.linspace(0,2*np.pi,20) # step needs to be equal to size of array being plotted
#x2 = np.linspace(-100,100,100000)
#y = -np.sin(np.pi*x2)+math.sqrt(2)*np.cos((9*np.pi*x2)/10)-math.sqrt(3)*np.sin((4*np.pi*x2)/5)+2*np.cos((7*np.pi*x2)/10)-2.2360679775*np.sin((3*np.pi*x2)/5)+2.44948974278*np.cos((np.pi/2)*x2)-2.64575131106*np.sin((2*np.pi*x2)/5)+2*math.sqrt(2)*np.cos((3*np.pi*x2)/10)-3*np.sin((np.pi/5)*x2)+3.16227766017*np.cos((np.pi/10)*x2)
plt.plot(x1, fhats)
#plt.plot(x2, y)
plt.title('Plot of m(x)')
plt.show()