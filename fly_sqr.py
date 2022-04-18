# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:39:42 2022

@author: svale
"""

# fly_sqr.py

import random as rd
import math as m

DistSqr = []
for ix in range(100000):
    x1, y1 = rd.random(), rd.random()
    x2, y2 = rd.random(), rd.random()
    DistSqr.append((x1-x2)**2 + (y1-y2)**2)

import matplotlib.pyplot as plt
plt.xlabel('Length of Line Segment')
plt.ylabel('Scaled Magnitude')

# To get distribution plot, change cumulative to True
n, bins, patches = plt.hist(DistSqr, 200, histtype='step', density=True, cumulative=False)
plt.show()

ProbZgt1 = 0.0
for x in DistSqr:
    if x >= 1.0:
        ProbZgt1 += 1.0

print('Prob = ', ProbZgt1 / len(DistSqr))
