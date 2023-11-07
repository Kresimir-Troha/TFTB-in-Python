#ALTES : altes signal in time domain
#	X = ALTES(N, FMIN, FMAX, ALPHA) - generates the Altes signal in the time domain
#
#   N : number of points in time
# fmin: lower frequency bound (value of the hyperbolic instanteneous frequency law at the sample N)
#			(default: .05)
# fmax: upper frequency bound (value of the hyperbolic instanteneous frequency law at the first sample)
#           (default: 0.50)
#alpha: attenuation factor of the envelope (default : 300)
#   X : time row vector containing the Altes signal sample
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import numpy as np

def altes(n = None, fmin = 0.05, fmax = 0.5 , alpha = 300):
	if n is None:
		raise ValueError('The number of arguments must be at least 1')

	if n <= 0:
		raise ValueError('The signal length N must be strictly positive')
	elif fmin > 0.5 or fmin < 0:
		raise ValueError('FMIN must be in [0, 0.5]')
	elif fmax > 0.5 or fmax < 0:
		raise ValueError('FMAX must be in [0, 0.5]')
	elif alpha <= 1:
		raise ValueError('Alpha must be larger than 1')
	else:
		g = np.exp((np.log(fmax/fmin)) ** 2 / (8*np.log(alpha)))
		nu0 = np.sqrt(fmin*fmax)
		beta = np.sqrt(2*np.log(g)*np.log(alpha))
		t0 = n/(np.exp(beta)-np.exp(-beta))
		t1 = t0 * np.exp(-beta)
		t2 = t0 * np.exp(beta)
		b = -t0 * nu0 * g * np.log(g)
		t = np.linspace(t1, t2, n + 1)
		t = t[:n]
		x = (np.exp(-(np.log(t / t0)**2) / (2 * np.log(g))) * np.cos(2 * np.pi * b * np.log(t / t0) / np.log(g)))
		x = x / np.linalg.norm(x)

	return x