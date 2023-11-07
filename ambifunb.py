#  Ambifunb - Narrow-band ambiguity function
#  ambifunb(x, tau, n, trace) computes the narrow-band ambiguity function of a signal X, or the
#   function between two signals
#
#  x     : signal if auto-AF, or [X1,X2] if cross-AF (length(x)=Nx).
#  tau   : vector of lag values (default: -Nx/2:Nx/2)
#  N     : number of frequency bins (default: length(x))
#  trace : if nonzero, the progression of the algorithm is shown (default: 0)
#  naf   : doppler-lag representation, with the doppler bins stored 
#	        in the rows and the time-lags stored in the columns.
#	        When called without output arguments, AMBIFUNB displays
#	        the squared modulus of the ambiguity function by means of
#	        contour.
#  xi    : vector of doppler values
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import numpy as np

def ambifunb(x = None, tau=None, N=None, trace=0):
	if x is None:
		raise ValueError('At least one parameter required')
	xrow, xcol = np.shape(x)
	if xcol == 0 | xcol > 2:
		raise ValueError('X must have one or two columns')

	if tau is None:
		if xrow % 2 == 0:
			tau = np.arrange(-xrow // 2 + 1, xrow / 2)
		else:
			tau = np.arrange(-(xrow - 1) // 2, (xrow + 1) // 2)
		N = xrow
		trace = 0
	elif N is None:
		N = xrow
		trace = 0
	elif trace is None:
		trace = 0

	taurow, tauco = np.shape(tau)

	if taurow != 1:
		raise ValueError('TAU must only have one row')
	elif N < 0:
		raise ValueError('N must be greater than zero')

	naf = np.zeros((N, taucol), dtype=complex)

	if trace:
	    print('Narrow-band ambiguity function')

	for icol in range(taucol):
		if trace:
			print(f'Processing column {icol + 1} out of {taucol}')
		taui = int(tau[icol])
		t = slice(1 + abs(taui), xrow - abs(taui))
		naf[t, icol] = x[t + taui, 0] * np.conj(x[t - taui, xcol - 1])

	naf = np.fft.fft(naf, axis = 0)
	naf = np.fft.fftshift(naf, axes=0)

	xi = np.arange(-(N - N % 2) / 2, (N + N % 2) / 2) / N

	plt.contour(2 * tau, xi, np.abs(naf)**2, 16)
	plt.grid(True)
	plt.xlabel('Delay')
	plt.ylabel('Doppler')
	plt.title('Narrow-band ambiguity function')
	plt.show()
	return naf, tau, xi 