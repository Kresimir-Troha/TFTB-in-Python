#DOPPLER Generate complex Doppler signal.
# fm, am, iflaw = doppler(N, FS, F0, D, V, T0, C) returns the frequency modulation, the amplitude and the
#     instantaneous frequency law(IFLAW) of the signal received by a fixed observer from a moving target 
#	  emitting a pure frequency f0
#
# n     : number of points
# fs    : sampling frequency (hZ)
# f0    : target frequency (hZ)
# d     : distance from the line to the observer (in meters)
# v     : target velocity    (in m/s)
# t0    : time center (default: n/2)
# c     : wave velocity (default: 340 m/s)
# fm    : output frequency modulation
# am    : output amplitude modulation
# iflaw : output instantaneous frequency law
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import numpy as np

def doppler(n, fs, f0, d, v, t0 = None, c = 340):
	if (t0 is None):
		t0 = n / 2

	if(n <= 0):
		raise ValueError('The signal length N must be strictly positive')
	elif(d <= 0.0):
		raise ValueError('The distance D must be positive')
	elif(fs <= 0.0):
		raise ValueError('The sampling frequency FS must be positive')
	elif((t0 < 1) or (t0 > n)):
		raise ValueError('T0 must be between 1 and N')
	elif((f0 < 0) or (f0 > fs / 2)):
		raise ValueError('F0 must be between 0 and FS/2')
	elif(v < 0):
		raise ValueError('V must be positive')
	else:
		tmt0 = (np.arange(1, n) - t0) / fs 
		dist = np.sqrt(d ** 2 + (v * tmt0) ** 2)
		fm = np.exp(1j * 2.0 * np.pi * f0 * (tmt0 - dist/c))
		if(np.abs(f0) < 0.000000000001):
			am = 0
		else:
			am = 1.0 / np.sqrt(dist)
		iflaw = (1 - v ** 2 * tmt0 / dist / c) * f0 / fs
		return fm, am, iflaw