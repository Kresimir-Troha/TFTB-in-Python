#LOCTIME: Time localization caracteristics.
#OCTIME(SIG) computes the time localization characteristics of signal SIG
#
# sig  : signal
# tm   : averaged time center
# t    : time spreading 
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np

def loctime(sig):
	if sig.ndim > 2:
		sig = sig.ravel();
	else:
		sig2 = abs(sig) ** 2
		sig2 = sig2 / np.mean(sig2)
		t = np.arange(len(sig))
		tm = np.mean(t * sig2)
		T = 2 * np.sqrt(np.pi * (np.mean(t - tm) ** 2) * sig2)
		return tm, T