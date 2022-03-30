# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 07:12:18 2022

@author: svale
"""

# spider.py

import random as rd

web = {0 : [3,6,7],
       1 : [2,8],
       2 : [1,4,7],
       3 : [0],
       4 : [2,5],
       5 : [4,6],
       6 : [0,5,7],
       7 : [0,2,6,8],
       8 : [1,7]}

nr_transitions = 0

max_transitions = 0
for nr_trials in range(100000):
    state = 0
    local_nr_transitions = 0
    while (state != 1):
        transition_set = web[state]
        transition_index = rd.randint(0, len(transition_set)-1)
        state = transition_set[transition_index]
        nr_transitions = nr_transitions + 1
        local_nr_transitions += 1
    if max_transitions < local_nr_transitions:
        max_transitions = local_nr_transitions

print(nr_transitions / (nr_trials + 1))
print('max transitions = ', max_transitions)
