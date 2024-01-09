#KLAUDER Klauder wavelet in time domain.
# x = klauder(n, lambda, f0) generates the klauder wavelet in the time domain
# 
# n    : number of points in time
# l	   : lambda, attenuation factor or the envelope (default : 10)
# f0   : central frequency of the wavelet (default : 0.2)
# x    : time row vector containing the klauder samples
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np

def klauder(n, l = 10, f0 = 0.2):
	if (n <= 0):
		raise ValueError('N must be greater or equal to 1.')
	elif(f0 > 0.5 or f0 < 0):
		raise ValueError('f0 must be between 0 and 0.5')
	else:
		f = np.linspace(0, 0.5, n // 2 + 1)
		mod = np.exp(-2 * np.pi * l * f) * f ** (2 * np.pi * l * f0 - 0.5)
		wave = np.concatenate((mod, np.flipud(mod[1:])))
		wavet = np.fft.ifft(wave)
		wavet = np.fft.fftshift(wavet)
		x = np.real(wavet) / np.linalg.norm(wavet)
		return x
