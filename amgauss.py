# AMGAUSS: Generate gaussian amplitude modulation
# AMGAUSS(n, t0, t) generates a gaussian amplitude modulation centered on a time T0
#                  and with a spread proportional to T. This modulation is scaled such 
#                  that Y(T0)=1 and Y(T0+T/2) and Y(T0-T/2) are approximately 0.5 .
# n   : number of points
# t0  : time center (defult : N/2)
# t   : time spreading (default: 2*sqrt(n))
# y   : signal
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import numpy as np
import matplotlib.pyplot as plt

def amgauss(n, t0 = None, t = None):
	if(t0 == None and t == None):
		t0 = n / 2
		t = 2 * np.sqrt(n)
	elif(t == None):
		t = 2 * np.sqrt(n)

	if(n <= 0):
		raise ValueError('N must be greater or equal to 1.')
	else:
		tmt0 = np.arange(n) - t0
		y = np.exp(-(tmt0/t) ** 2 * np.pi)
	

	return y