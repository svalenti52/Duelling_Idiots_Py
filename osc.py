# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:49:05 2022

@author: svale
"""

import random as rd

real_val = 0
other_real_val = 0
for ix in range(1000000):
    A = rd.random()
    B = rd.random()
    C = rd.random()
    if B**2 >= 4*A*C:
        real_val += 1
    if B**2 >= 4*C:
        other_real_val += 1

print('Probabilities of real solutions:')
print('value with A = ',real_val / 1000000)
print('value without A = ', other_real_val / 1000000)
