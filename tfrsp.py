# TFRSP - Spectrogram time-frequency distribution
# computes the Spectogram distribution of a discrete-time signal x
#
#  x       : signal
#  T       : time instant(s)          							(default : 1:length(X))
#  N       : number of frequency bins 							(default : legth(X))
#  H       : analysis window, H being 							(default: Hamming(N/4))
#            normalized as to be a unit of energy
#  TRACE   : if nonzero, shows progression of the algorithm     (default : 0)
#  TFR     : time-frequency representation. When called 
#             without output arguments, TFRSP runs TFRQVIEW
#  F       : vector of normalized frequencies
#
# use example:  
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
                                       
import numpy as np
import matplotlib.pyplot as plt

def tfrsp(x, t=None, N=None, h=None, trace=0):
	if x is None:
		raise ValueError('At least 1 parameter required')

    # Default is 1-x
	if t is None:
		t = np.arange(1, len(x) + 1)
	# If the number of frequency bins 'N' is not provided, use the length of 'x'
	if N is None:
		N = len(x)

    # create a hamming window if one is not provided
	if h is None:
		hlength = N // 4
		hlength = hlength + 1 - hlength % 2
		h = np.hamming(hlength)
    # half length of h
	Lh = (len(h) - 1) // 2

    #empty matrix, N * len(t)
	tfr = np.zeros((N, len(t)), dtype=complex)
    
    #if nonzero, show the progression of the algorithm
	if trace:
		print('Spectrogram')

	for i in range(len(t)):
		ti = t[i]

		tau = np.arange(min(N // 2 - 1, Lh, ti - 1), min(N // 2 - 1, Lh, len(x) - ti))
		indices = np.remainder(N + tau, N)
		if trace:
			print(f'Processing column {i + 1} of {len(t)}')
		tfr[indices, i] = x[ti + tau] * np.conj(h[Lh + 1 + tau]) / np.linalg.norm(h[Lh + 1 + tau])
    # Compute the spectrogram as the square of the absolute value of the FFT
	tfr = np.abs(np.fft.fft(tfr)) ** 2

	if trace:
		print()
    
	if N % 2 == 0:
		f = np.concatenate((np.arange(0, N // 2) / N, np.arange(-N // 2, 0) / N))
	else:
		f = np.concatenate((np.arange(0, (N - 1) // 2) / N, np.arange(-(N - 1) // 2, 0) / N))
    
	return tfr, t, f