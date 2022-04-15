# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:24:22 2022

@author: svale
"""

# quadratic.py

import random as rd

nr_events = 100000

A = [rd.random() for x in range(nr_events)]
B = [rd.random() for x in range(nr_events)]
C = [rd.random() for x in range(nr_events)]

A1 = [rd.random() for x in range(nr_events)]

count_1BC = 0
count_ABC = 0
count_BC = 0

for ix in range(nr_events):
    if B[ix]**2 >= 4 * A[ix] * C[ix]:
        count_ABC += 1
    if B[ix]**2 >= 4 * C[ix]:
        count_1BC += 1
    if B[ix]/A[ix] * B[ix]/A[ix] >= 4 * C[ix]/A1[ix]:
        count_BC += 1

print('For A=1 probability solution is real = ', count_1BC/nr_events)
print('For A in [0,1] probability solution is real = ', count_ABC/nr_events)
print('For B and C independent probability solution is real = ', count_BC/nr_events)
