#LOCFREQ Frequency localization caracteristics.
# LOCFREQ(SIG) calculates the frequency localization characteristics of signal SIG
#
# sig    : signal.
# fm     : averaged normalized frequency center
# b      : frequency spreading
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np

def locfreq(sig):
	if(sig.ndim >= 1):
		sig = sig.ravel()
	else:
		raise TypeError
	rows = sig.shape[0]
	No2r = np.round(rows / 2.0)
	No2f = np.floor(rows / 2.0)
	sig = np.fft.fft(sig)
	sig2 = np.abs(sig) ** 2
	sig2 = sig2 / np.mean(sig)
	freqs = np.concatenate([np.arange(No2f), np.arange(-No2r, 0)]) / rows
	fm = np.mean(freqs * sig2)
	b = 2 * np.sqrt(np.pi * np.mean((freqs - fm) ** 2 * sig2))
	return fm, b
