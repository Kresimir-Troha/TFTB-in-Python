#  Fmlin - signal with linear frequency modulation
#
#  [Y,IFLAW]=FMLIN(N,FNORMI,FNORMF,T0) generates a linear frequency modulation
#  The phase of this modulation is such that Y(T0)=1
#  N 	 : number of points
#  FNORMI: initial normalized frequency (default: 0.0)
#  FNORMF: final normalized frequency (default: 0.5)
#  T0    : time reference for the phase (default: N/2)
#  y 	 : signal
#  iflaw : instantaneous frequency law
#
#  use example: xpoints, ypoints = fmlin.fmlin(128,0,0.5)
#               plt.plot(xpoints, ypoints)
#
# returns tuple line and signal
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import numpy as np

def fmlin(N, fnormi=0.0, fnormf=0.5, t0=None):
    if t0 is None:
        t0 = round(N / 2)

    if N <= 0:
        raise ValueError('The signal length N must be strictly positive')

    if abs(fnormi) > 0.5 or abs(fnormf) > 0.5:
        raise ValueError('fnormi and fnormf must be between -0.5 and 0.5')

    y = np.arange(1, N + 1)
    y = fnormi * (y - t0) + ((fnormf - fnormi) / (2.0 * (N - 1))) * ((y - 1) ** 2 - (t0 - 1) ** 2)
    y = np.exp(1j * 2.0 * np.pi * y)
    y = y / y[t0 - 1] 

    iflaw = np.linspace(fnormi, 128, N)

    return iflaw, y