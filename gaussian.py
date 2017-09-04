from math import e, sqrt, pi

m = 0.52
s = 4
x = 0.001
gauss = 1/(sqrt(2*pi)*s)*e**(-0.5*(float(x-m)/s)**2)
print gauss

'''
Sample run:
0.176032663382
'''
from math import e, sqrt, pi
import numpy as np

m = 0.52
s = 0.5

vetor = []

for x in np.arange(-3.0, 3.0, 0.05):
	vetor.append(1/(sqrt(2*pi)*s)*e**(-0.5*(float(x-m)/s)**2))

print vetor

import matplotlib.pyplot as plt

plt.scatter(np.arange(-3.0, 3.0, 0.05), vetor)
plt.show()
