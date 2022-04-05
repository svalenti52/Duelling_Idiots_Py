# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 06:47:07 2022

@author: svale
"""

# e_number2.py

import random as rd

nr_trials = 10000000

sum_gt_one = 0
for ix in range(nr_trials):
    sum_random = 0.0
    gt_one = 0
    while sum_random < 1.0:
        sum_random += rd.random()
        gt_one += 1
    sum_gt_one = sum_gt_one + gt_one

print('approximation of e = ', sum_gt_one / nr_trials)
