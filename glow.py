# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:03:42 2022

@author: svale
"""

#glow.py

n = 5

def series_glows(p):
    row_no_glow = 1 - p**n
    sheet_no_glow = row_no_glow**n
    sheet_glow = 1 - sheet_no_glow
    sheet_series_glow = sheet_glow**n
    return sheet_series_glow

def parallel_glows(p):
    row_no_glow = 1 - p**n
    sheet_no_glow = row_no_glow**n
    sheet_parallel_no_glow = sheet_no_glow**n
    sheet_parallel_glow = 1 - sheet_parallel_no_glow
    return sheet_parallel_glow

single_switch_closed = [p / 100.0 for p in range(100)]

import matplotlib.pyplot as plt

xt = plt.xticks([x for x in range(101) if x % 10 == 0])
yt = plt.yticks([x / 100.0 for x in range(101) if x % 10 == 0])

plt.xlabel('Probability Percentage Individual Switch Closed')
plt.ylabel('Probability Sheet In Series Glows')
#plt.xlim((0,100))
series_glow = []
parallel_glow = []
for p in single_switch_closed:
    series_glow.append(series_glows(p))
    parallel_glow.append(parallel_glows(p))
plt.plot(series_glow, 'b')
plt.plot(parallel_glow, 'g')
plt.legend(['Series', 'Parallel'])
plt.show()
