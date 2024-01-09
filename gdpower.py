#GDPOWER: Signal with power-law group delay
# x, gpd, nu = gdpower(n, k, c) generates a signal with a power-law group delay
#               of the form tx(f) = T0 + c*f**(k - 1), the output signal is of unit energy
#
# n   : number of points in time (must be even)
# k   : degree of the power-law  (default: 0)
# c   : rate-coefficient of the power-law group delay, must be non-zero (default: 1)
# x   : time row vector containing the modulated signal samples
# gpd : group delay
# f   : frequency bins
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np
import anapulse as anapulse

def gdpower(n, k = 0, c = 1):

	if (n <= 0):
		raise ValueError('The signal length N must be strictly positive')
	elif (c == 0):
		raise ValueError('C must be non-zero')
	t0 = 0

	Lnu = np.round(n / 2)
	nu = np.linspace(0, 0.5, Lnu + 1)[1:Lnu + 1]
	am = nu ** ((k - 2) / 6)

	t = np.arange(1, n)
	TFx = np.zeroes(n)

	if(k < 1 and k != 0):
		d = n ** k * c
		t0 = N / 10
		TFx = np.exp(-1j * 2 * np.pi * (t0 * nu + d * nu ** k / k)) * am
		x = np.ftt.ifft(TFx)
	elif( k == 0):
		d = c
		t0 = N / 10
		TFx = np.exp(-1j * 2 * np.pi * (t0 * nu + d * np.log(nu))) * am
		x = np.ftt.ifft(TFx)
	elif( k == 1):
		t0 = n
		x = anapulse(n, t0)
	elif( k > 1):
		d = n * (2 ** ( k - 1)) * c
		TFx = np.exp(-1j * 2 * np.pi * (t0 * nu + d * nu ** k / k)) * am
		x = np.ftt.ifft(TFx)

	if(k != 1):
		gpd = t0 + np.abs(np.sign(c) - 1) / 2 * (n + 1) + d * nu ** (k - 1)
	else:
		gpd = t0 * np.ones(n / 2)

	return x, gpd, nu

