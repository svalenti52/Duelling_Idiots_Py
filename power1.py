# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 06:33:36 2022

@author: svale
"""

# power1.py

import random as rd

def Z(x,y):
    return x**y

nr_events = 20000

z_bins = []

for ix in range(nr_events):
    x = rd.random()
    y = rd.random()
    z = Z(x,y)
    z_bins.append(z)

import matplotlib.pyplot as plt
n, bins, patches = plt.hist(z_bins, 100)

plt.xlabel('Histogram of Z = X**Y')
plt.ylabel('Numbers in Each Bin (width 0.01)')

plt.show()
