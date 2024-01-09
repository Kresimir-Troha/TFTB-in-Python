#ANAPULSE Analytic projection of unit amplitude impulse signal.
# y=ANAPULSE(N,TI) returns an analytic N-dimensional signal whose real part is a dirac impulse at t = TI
# n  : number of points
# ti : time positon of the impulse (default : round(n/2))
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np 
from scipy.signal import hilbert

def anapulse(n, ti = None):
	if ti == None:
		ti = np.round(n / 2)

	if n <= 0:
		raise ValueError('N must be greater than zero')
	else:
		t = np.arange(n)
		y = hilbert(t == ti)

	return y
