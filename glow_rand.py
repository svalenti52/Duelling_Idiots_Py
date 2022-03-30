# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:31:56 2022

@author: svale
"""

# glow_rand.py

import random as rd
import numpy as np

state_vec = np.array([1.0, 0.0, 0.0, 0.0])
state_trans = np.array(([0.97, 0.03, 0.0, 0.0],
                       [0.0, 0.98, 0.02, 0.0],
                       [0.0, 0.0, 0.99, 0.01],
                       [0.0, 0.0, 0.0, 1.0]))

glow = [state_vec @ np.linalg.matrix_power(state_trans, p) for p in range(1000)]

a = [glow[i][0] for i, n in enumerate(glow)]
b = [glow[i][1] for i, n in enumerate(glow)]
c = [glow[i][2] for i, n in enumerate(glow)]
d = [glow[i][3] for i, n in enumerate(glow)]

import matplotlib.pyplot as plt

xt = plt.xticks([x for x in range(1001) if x % 100 == 0])
yt = plt.yticks([x/1000.0 for x in range(1000) if x % 100 == 0])

plt.xlabel('Milliseconds')
plt.ylabel('Probability of Being in State')
plt.xlim((0,400))
plt.plot(a, 'r')
plt.plot(b, 'b')
plt.plot(c, 'g')
plt.plot(d, 'c')
plt.legend(['Initial', 'Interim 1', 'Interim 2', 'End'])
plt.show()
