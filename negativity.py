# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 06:33:36 2022

@author: svale
"""

# negativity.py

import random as rd

def Z(x,y):
    return x / (x - y)

nr_events = 10000

z_bins = []

for ix in range(nr_events):
    x = rd.random()
    y = rd.random()
    z = Z(x,y)
    while z < -3.0 or z > 3.0:
        x = rd.random()
        y = rd.random()
        z = Z(x,y)
    z_bins.append(z)

sorted_z_bins = sorted(z_bins)

inc = 0.05
left_edge = -3.0

left_edge_z_bins = [left_edge+inc*x for x in range(120)]

counted_z_bins = []
for ix in range(120):
    count_it = 0
    for jx in range(nr_events):
        if left_edge_z_bins[ix] > sorted_z_bins[jx]:
            continue
        if left_edge_z_bins[ix]+inc > sorted_z_bins[jx]:
            count_it += 1
        else:
            break
    counted_z_bins.append(count_it)

import matplotlib.pyplot as plt
plt.xlabel('Histogram of Z = X/(X-Y)')
plt.ylabel('Numbers in Each Bin (width 0.5)')

plt.bar(left_edge_z_bins, counted_z_bins, width=0.05)
plt.show()
print(counted_z_bins[59])