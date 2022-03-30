# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 09:33:21 2022

@author: svale
"""

# coffee.py

import random as rd

N = 6
NR_TRIALS = 10000

total_count = 0

for trials in range(NR_TRIALS):
    count = 1
    coffee = [rd.randint(0 ,1) for i in range(N)]
    while coffee.count(0) != 1 and coffee.count(1) != 1:
        count = count + 1
        coffee = [rd.randint(0 ,1) for i in range(N)]
    total_count = total_count + count

print(total_count / NR_TRIALS)
