import math
import numpy as np
import matplotlib.pyplot as plt
from fmlin import fmlin 
from noisecg import noisecg
from tfrsp import spectrogram
from sigmerge import sigmerge

N = 128
fnormi = 0
fnormf = 0.5
x = noisecg(N, 0.5, 0.3)
y, yi = fmlin(128)
z = sigmerge(yi, x, 0)

plt.plot(z)
plt.show()