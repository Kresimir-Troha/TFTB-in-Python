#INSTFREQ Instantaneous frequency estimation.
# INSTFREQ(X,T,L,TRACE) computes the instantenous frequency of the analytic signal
#  X at time instant(s) T, usimg the trapezoidal integration rule. The result FNORMHAT 
#  lies between 0.0 and 0.5
#
# X : Analytic signal to be analyzed
# T : Time instants (default : 2 / length(x)-1)
# L : If L=1, computes the (normalized) instantaneous frequency 
#	  of the signal X defined as angle(X(T+1)*conj(X(T-1)) ;
#	  if L>1, computes a Maximum Likelihood estimation of the
#	  instantaneous frequency of the deterministic part of the signal
#	  blurried in a white gaussian noise.
#	  L must be an integer (default : 1).
# TRACE : if nonzero, the progression of the algorithm is show (default : 0)
# FNORMHAT : Output (normalized) instantaneous frequency
# Ti : Time instants
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import numpy as np 

def instfreq(x, t = Null, l = 1, trace = 0):
	if x.ndim != 1:
		raise TypeError('X must have only one column')
	else:
		x = x.ravel()

	xrow = len(x)

	if t is None:
		t = np.arange(2, xrow)

	if (l < 1):
		raise ValueError('L must be >= 1')
	else if( t.ndim != 1):
		raise TypeError('T must have only one row')

	if( l == 1):
		if (any(t==1) | any(t==xrow)):
			raise ValueError('T can not be equal to 1 or last element of x')
		else:
			fnormhat = 0.5 * (np.angle(-x[t] * np.conj(x[t - 2])) + np.pi) / (2 * np.pi)
			return fnormhat, t
	else:
		h = kaytth(l)
		if(np.any(t <= l) | np.any(t + l >= xrow)):
			raise ValueError('The relation L<T<=length(X)-L must be satisfied')
		else:
			