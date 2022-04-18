# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 08:39:42 2022

@author: svale
"""

# reliable.py

import random as rd
import math as m

a = 1 / 100
Single = []
Multiple = []
for n in range(200):
    sing = 1 - m.exp(-a * n)
    Single.append(sing)
    Multiple.append(sing*sing*(3-2*sing))


    
import matplotlib.pyplot as plt
plt.xlabel('Time t (in arbitrary units)')
plt.ylabel('Probability of Failure')

plt.plot(Single)
plt.plot(Multiple, 'r')
plt.legend(['Single System', 'Three Systems'])
plt.show()
