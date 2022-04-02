# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 06:28:34 2022

@author: svale

Using monte carlo method for computing pi
"""

# pi.py

import random as rd

in_square = 10000000

in_circle = 0

for ix in range(in_square):
    x, y = (rd.random(), rd.random())
    if x**2 + y**2 <= 1.0:
        in_circle += 1

pi_est = 4.0 * in_circle / in_square

print(pi_est)
