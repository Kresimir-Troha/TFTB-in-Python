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

def noisecg(n, a1 = None, a2 = None):

	if n <= 0:
		raise ValueError('The signal length must be strictly positive');
		return

	if a1 is None and a2 is None:
		if n <= 2:
			noise = (np.random.randn(n) + 1j * np.random.randn(n)) / np.sqrt(2)
		else:
			noise = np.random.randn(2 ** (int(np.ceil(np.log2(n)))))
	elif a2 is None:
		if np.abs(a1) >= 1.0:
			raise ValueError('for a first order filter, abs(a1) must be strictly lower than 1')
		elif abs(a1) <= np.finfo(float).eps:  #smallest showable number
			if n <= 2:
				noise = (np.random.randn(n) + 1j * np.random.randn(n)) / np.sqrt(2)
			else:
				noise = np.random.randn(n)
		else:
			if N <= 2:
				noise = (np.random.randn(n) + 1j * np.random.randn(n)) / np.sqrt(2)
			else:
				Nnoise = int(np.ceil(N - 2.0 / np.log(a1)))
				noise = np.random.randn(2 ** (int(np.ceil(np.log2(Nnoise)))))
			k = [np.sqrt(1.0 - a1 ** 2)]
			l = [1, -a1]
			noise = lfilter(k, l, noise)
	else:
		if any(np.roots([1, -a1, -a2]) > 1):
			raise ValueError('Unstable filter')
		else:
			if n <= 2:
				noise = (np.random.randn(N) + 1j * np.random.randn(N)) / np.sqrt(2)
			else:
				Nnoise = Nnoise = int(np.ceil(N - 2.0 / np.log(max(np.roots([1, -a1, -a2])))))
				noise = np.random.randn(2 ** (int(np.ceil(np.log2(Nnoise)))))

			b = np.sqrt(1.0 - a1 ** 2 - a2 ** 2)
			a = [1, -a1, -a2]
			noise = lfilter(b, a, noise)
    #The Hilbert transform is related to the actual data by a 90-degree phase shift; sines become cosines and vice versa
	if n > 2:
		noise = (np.fft.fft(noise)).conj() / np.std(noise) / np.sqrt(2)
		noise = noise[len(noise) - np.arrange(n)]
	return noise
