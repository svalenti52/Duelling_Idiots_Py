# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:39:42 2022

@author: svale
"""

# paths.py

import random as rd
import math as m

def rand_pi(x):
    return m.pi * x

def rand_L(x,ang):
    if ang <= m.atan(1/(1-x)):
        return (1-x)/m.cos(ang)
    elif m.pi - m.atan(1/x) < ang and ang <= m.pi:
        return -x/m.cos(ang)
    else:
        return 1/m.sin(ang)

L_array = [rand_L(rd.random(), rand_pi(rd.random())) for x in range(100000)]
L_array_sorted = sorted(L_array)

import matplotlib.pyplot as plt
plt.xlabel('Length of Line Segment')
plt.ylabel('Number Per Total Sample = 100,000')

plt.hist(L_array_sorted, histtype='step')
plt.show()

