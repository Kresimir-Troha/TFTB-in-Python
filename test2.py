import matplotlib.pyplot as plt
import numpy as np
import fmlin as fmlin

N = 128
fnormi = 0
fnormf = 0.5
x, sig1 = fmlin.fmlin(N, fnormi, fnormf)

dsp1 = np.fft.fftshift(np.abs(np.fft.fft(sig1))**2) #energy spectrum

freq_axis = np.arange(-N/2, N/2) / N #Return evenly spaced values within a given interval, frequency axis

plt.plot(freq_axis, dsp1)
plt.show()