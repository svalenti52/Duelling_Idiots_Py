# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 07:19:50 2022

@author: svale
"""

# flip_same.py

import random as rd

nr_people = [2, 3, 4]
nr_flips = [10, 50, 100, 150]
nr_trials = 100000

for nf in nr_flips:
    for np in nr_people:
        nr_matches = 0
        for jx in range(nr_trials):
            people = []
            for p in range(np):
                flips = []
                for f in range(nf):
                    flips.append(rd.randint(0, 1))
                people.append(flips.count(0))
            matching = True
            for ix in range(len(people)-1):
                if people[ix] != people[ix+1]:
                    matching = False
                    break
            if matching:
                nr_matches += 1
        print('for nr people = ', np, ' and flips = ', nf, ' odds are = ', nr_matches / nr_trials)
