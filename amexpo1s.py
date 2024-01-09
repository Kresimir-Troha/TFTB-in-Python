#AMEXPO1S: Generate one-sided exponential amplitude modulation.
#AMEXPO1S(N,T0,T) generates a one-sided exponential amplitude modulation centered on a time T0,
#       and with a spread proportional to T
#       This modulation is scaled such that Y(T0)=1
# N    : number of points.
# T0   : arrival time of the exponential (default : N/2)
# T    : time spreading (default: 2*sqrt(N))
# Y    : signal
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np
import matplotlib.pyplot as plt

def amexpo1s(n = None, t0 = None, t = None):
	if n is None:
		raise ValueError('The number of parameters must be at least 1.')
	elif t0 is None:
		t0 = n / 2
		t = 2 * np.sqrt(n)
	elif t is None:
		t = 2 * np.sqrt(n)

	if n <= 0:
		raise ValueError('N must be greater or equal to 1.')
	else:
		tmt0 = np.arange(1, n + 1) - t0
		y = np.exp(-np.sqrt(np.pi) * tmt0 / t) * (tmt0 >= 0.0)
	return y

#N_val = 100  
#computed_y = amexpo1s(N_val)
#plt.plot(computed_y)
#plt.show()