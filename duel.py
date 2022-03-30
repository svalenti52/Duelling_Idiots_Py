# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 09:35:59 2022

@author: svale
"""

# duel.py

import random as rd

'''
A_shot_B_count = 0
B_shot_A_count = 0

NR_TRIALS = 100000

for nr_trials in range(NR_TRIALS):
    shot = False
    while not shot:
        if rd.randint(1, 6) == 1:
            shot = True
            A_shot_B_count += 1
        else:
            if rd.randint(1,6) == 1:
                shot = True
                B_shot_A_count += 1

print(A_shot_B_count / NR_TRIALS)
'''

A_shot_B_count = 0
B_shot_A_count = 0
max_trigger_pull = 0

NR_TRIALS = 1000000

for nr_trials in range(NR_TRIALS):
    shot = False
    interim_count = 0
    subsequent_shots_count = 1
    while not shot:
        for tries in range(subsequent_shots_count):
            interim_count += 1
            if rd.randint(1, 6) == 1:
                shot = True
                A_shot_B_count += 1
                break
        if shot:
            break
        subsequent_shots_count += 1
        for tries in range(subsequent_shots_count):
            interim_count += 1
            if rd.randint(1, 6) == 1:
                shot = True
                B_shot_A_count += 1
                break
        subsequent_shots_count += 1
        if interim_count > max_trigger_pull:
            max_trigger_pull = interim_count

print(A_shot_B_count / NR_TRIALS)
print(max_trigger_pull)
