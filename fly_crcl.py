# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 08:39:42 2022

@author: svale
"""

# fly_crcl.py

import random as rd
import math as m

DistSqr = []
for ix in range(100000):
    radius = 1 / m.sqrt(m.pi)
    angle = 2 * m.pi

    # r = rd.random() * radius
    # see discussion on pp 17-18 "Digital Dice"
    r = m.sqrt(rd.random() * radius) # because of clumping (sqrt)
    while r > radius: # needed because possible to be outside of circle (radius)
        r = m.sqrt(rd.random() * radius)
    ang = rd.random() * angle
    x1, y1 = r * m.cos(ang), r * m.sin(ang)

    # r = rd.random() * radius
    r = m.sqrt(rd.random() * radius)
    while r > radius:
        r = m.sqrt(rd.random() * radius)
    ang = rd.random() * angle
    x2, y2 = r * m.cos(ang), r * m.sin(ang)

    DistSqr.append((x1-x2)**2 + (y1-y2)**2)

import matplotlib.pyplot as plt
plt.xlabel('Landing difference in position')
plt.ylabel('Number Sampled (Total = 100,000)')

# To get distribution plot, change cumulative to True
n, bins, patches = plt.hist(DistSqr, 200, histtype='step', density=False, cumulative=False)
plt.show()

ProbZgt1 = 0.0
for x in DistSqr:
    if x >= 1.0:
        ProbZgt1 += 1.0

print('Probability  = ', ProbZgt1 / len(DistSqr))
