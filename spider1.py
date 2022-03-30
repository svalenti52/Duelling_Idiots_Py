# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 07:12:18 2022

@author: svale
"""

# spider1.py

import random as rd

web_tx = [[3,6,7],
       [2,8],
       [1,4,7],
       [0],
       [2,5],
       [4,6],
       [0,5,7],
       [0,2,6,8],
       [1,7]]

web = []
for ix, item in enumerate(web_tx):
    web.append((ix,item))

nr_transitions = 0

for nr_trials in range(1000000):
    state = 0
    while (state != 1):
        transition_set = web[state][1]
        transition_index = rd.randint(0, len(transition_set)-1)
        state = transition_set[transition_index]
        nr_transitions = nr_transitions + 1

print(nr_transitions / (nr_trials + 1))
