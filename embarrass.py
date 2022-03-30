# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 07:48:34 2022

@author: svale
"""

# embarrass.py

import random as rd

sample_sz = 1000000
pop_prob = 0.746
act = 0

for ix in range(sample_sz):
    answer_truthfully = rd.randint(0,1)
    if answer_truthfully == 0:
        random_answer = rd.randint(0,1)
        act = random_answer + act
    else:
        prob_ans = rd.random()
        if prob_ans <= pop_prob:
            act += 1

print(act / sample_sz)
