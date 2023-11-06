#SIGMERGE : add two signals with given energy ratio in dB
# SIGMERGE(X1, X2, RATION) adds two signals so that a given energy ration 
#   expressed in decibels is satisfied
#
# X1, X2  : input signals
# RATION  : Energy ratio in deciBels (default: 0 dB)
# x       : output signal
# x = x1 + H*X2 such that 10*log(Energy(X1)/Energy(H*X2))=RATIO
# 
# Use example: sig= fmlin(64, 0.01, 0.05, 1)
#			   noise=hilbert(randn(64, 1))
#			   x = sigmerge(sig, noise, 15)
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import numpy as np

def sigmerge(x1, x2, ratio = 0):
	#calculate energy of given signals
	Ex1 = np.mean(np.abs(x1) ** 2)
	Ex2 = np.mean(np.abs(x2) ** 2)

	#compute the scaling factor h
	h = np.sqrt(Ex1 / (Ex2 * 10 ** (ratio / 10)))

	sig = x1 + h * x2

	return sig
