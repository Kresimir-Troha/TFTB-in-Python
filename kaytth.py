#KAYTTH	 Kay-Tretter filter computation.
# KAYTTH(length) returns Kay-Tretter filter computation
#
# l      : length of signal to be returned
# h      : K-T filtered signal
# 
# use example:
#x = kaytth(120)
#plt.plot(x)
#plt.show()
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np 
import matplotlib.pyplot as plt

def kaytth(length):
	pp1 = length * (length + 1)
	den = 2.0 * length * (length+1) * (2.0 * length + 1.0) / 3.0
	i = np.arange(1, length)
	h = pp1 - i * (i - 1)
	h = h / den
	return h

