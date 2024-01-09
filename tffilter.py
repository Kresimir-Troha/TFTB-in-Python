#TFFILTER Time frequency filtering of a signal.
# Y=TFFILTER(TFR,X,T) filters the signal X with a non stationary filter
#
# x      : input signal (must be analytic)
# t      : time instant(s) (default: 1:length(x))
# tfr    : Wigner-Vile distribution of the filter, f axis is graduated from 0.0 to 0.5
#
# this function is based on the following reference :
# W. Kozek, F. Hlawatsch, A comparative study of linear and non-linear
# time-frequency filters, proc IEEE int symp on time-frequency and 
# time-scale analysis, pp 163-166, victoria, canada, 1992.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np
import nextpow2 as nextpow2

def tffilter(tfr, x, t):
	Ntup = tfr.shape
	print(Ntup)
	(N, NbPoints) = Ntup
	tcol = t.shape 
	trow = 1
	xrow, xcol = x.shape

	if (trow != 1):
		raise TypeError('T must only have one row')
	elif(xcol != 1):
		print(2)
		#raise TypeError('X must only have one column')
	elif(2 ** nextpow2(N) != N):
		print('For a faster computation, N should be a power of two')
	elif(xrow != NbPoints):
		raise TypeError('tfr should have as many columns as X has rows.')
	elif((min(t) < 1) | (max(t) > NbPoints)):
		raise ValueError('the values of T must be between 1 and xrow.')

	tfr = np.fft.ifft(tfr)
	y = np.zeros(tcol)

	for i in range(tcol[0]):
		ti = t[ i]
		valuestj = np.arange(max([1, 2 - ti, ti - N/2 + 1]), min([NbPoints, 2 * NbPoints - ti, ti + N/2]))

		for tj in valuestj:		
			tmid = int(np.fix(0.5 * (ti + tj)))
			tdiff = int(np.fix(ti -tj))
			indice = int((N + tdiff) % N )

			y[tcol[0] - 1] = y[tcol[0] - 1] + tfr[indice, tmid] * x[int(tj)]

	return y