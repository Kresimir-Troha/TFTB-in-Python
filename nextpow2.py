#NEXTPOW2: Returns the next power of 2
#
#  X: number to find the next power of two for
#  i: 2^i > x
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

def nextpow2(x):
	i = 1
	while (2 ** i) < x:
		i += 1
	return i