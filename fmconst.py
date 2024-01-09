#FMCONST - signal with constant frequency modulation
# generates a frequency modulation 	with a constant frequency fnorm
# The phase of this modulation is such that y(T0) = 1
#
# N        : number of points
# FNORM    : normalized frequency
# T0       : time center
# Y        : signal
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np

def fmconst(n, fnorm = 0.25, t0 = None):

	if (t0 == None):
		t0 = round(n / 2.0)

	if(n <= 0):
		raise valueError('N must be greater or equal to 1.')
	elif(abs(fnorm) > 0.5):
		raise valueError('The normalised frequency must be between -0.5 and 0.5')
	else:
		tmt0 = np.arange(n) - t0
		y = np.exp(1j * 2 * np.pi * fnorm * tmt0)
		y = y / y[t0]
		iflaw = fnorm * np.ones(n)
		return y, iflaw
		