import numpy as np
import matplotlib.pyplot as plt

"""
Add two signals with given energy ratio in dB.
 X1, X2 - input signals
 ratio - energy ration in deciBels (default : 0 dB)
 X - output signal
 X = X1 + H*X2, where 10*log(Energy(X1)/ENERGY(H*X2)) = RATIO

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

"""

def sigmerge(x1, x2, ratio = 0):

	assert x1.ndim == 1
	assert x2.ndim == 1
	assert type(ratio) in (float, int)
	ex1 = np.mean(np.abs(x1) ** 2)
	ex2 = np.mean(np.abs(x2) ** 2)
	h = np.sqrt(ex1 / (ex2 * 10 ** (ratio / 10)))
	print('h is:' + repr(h))
	x = x1 + h * x2
	return x
