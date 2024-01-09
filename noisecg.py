#NOISECG : computes an analytic complex gaussian noise of length N
#			with mean 00 and variance 1.0.
#noisecg(N) yields a complex white gaussian noise
#noisecg(N, A1) yields a complex colored gaussian noise obtained
# 	by filtering a white gaussian noise through a first order filter
#			sqrt(1 - A1**2)/(1 - A1* z**(-1))

#noiscg(N, A1, A2) yields a complex colored gaussian noise obtained
#	by filtering a white gaussian noise through a second order filter
#				sqrt(1-A1**2 - A2 ** 2)/(1 - A1 * z ** (-1) - A2 * z ** (-2))
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import numpy as np
from scipy.signal import hilbert
import math
from nextpow2 import nextpow2

def noisecg(n, a1 = None, a2 = None):

	assert n > 0
	if n <= 2:
		noise = (np.random.randn(n, 1) + 1j * np.random.randn(n, 1.)) / np.sqrt(2.)
	else:
		noise = np.random.randn((2 ** nextpow2(n)))
		noise = hilbert(noise) / noise.std() / np.sqrt(2)
		noise = noise[len(noise) - np.arange(n - 1, -1, -1) - 1]
	return noise

def noisecgN(n, a1=None, a2=None):
    assert n > 0
    
    if n <= 2:
        noise = (np.random.randn(n, 1) + 1j * np.random.randn(n, 1.)) / np.sqrt(2.)
    else:
        noise = np.random.randn((2 ** nextpow2(n)))

    if a1 is not None:
        if abs(a1) >= 1:
            raise ValueError('For a first-order filter, abs(a1) must be strictly lower than 1')
        elif abs(a1) < np.finfo(np.float32).eps:
            noise = (np.random.randn(n, 1) + 1j * np.random.randn(n, 1.)) / np.sqrt(2.)
        else:
            nNoise = math.ceil(n - 2.0 / math.log(a1))
            noise = filter([np.sqrt(1.0 - a1 ** 2)],  noise)

    if n > 2:
        noise = hilbert(noise) / noise.std() / np.sqrt(2)
        noise = noise[len(noise) - np.arange(n - 1, -1, -1) - 1]

    return noise