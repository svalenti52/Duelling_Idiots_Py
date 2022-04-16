# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 06:33:36 2022

@author: svale
"""

# kids.py

import random as rd

nr_poss_fam = 10000

prob_boy = [x/100.0 for x in range(101)]
prob_grl = list(reversed(prob_boy))

C_array = []

size_fam = [x+2 for x in range(nr_poss_fam)]

for jx,pb in enumerate(prob_boy):
    C = 0.0
    for sz in size_fam:
        C += ((prob_boy[jx]**2 * prob_grl[jx]**(sz-2)) + \
              (prob_boy[jx]**(sz-2) * prob_grl[jx]**2)) * sz
    C_array.append(C)

import matplotlib.pyplot as plt
plt.xlabel('Probability Percentage Giving Birth to a Boy')
plt.ylabel('Expected Size of Family')

plt.plot(C_array)
plt.show()
