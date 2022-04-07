# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 07:35:10 2022

@author: svale
"""

# champ.py

import random as rd

drawodds = 0.1
nr_games = 6
pwinsingle = 0.55

pwin = [x/100.0 for x in range(101 - int(drawodds*100))]

nr_trials = 100000

pchampwins_by_prob = []
pchampdraws_by_prob = []
for px in pwin:
    champ_won_match = 0
    match_drawn = 0
    for ix in range(nr_trials):
        champ_won = 0
        drawn = 0
        tally = 0.0
        for jx in range(nr_games):
            result = rd.random()
            if result <= px:
                champ_won += 1
                tally += 1.0
            elif result <= px+drawodds:
                drawn += 1
                tally += 0.5
        if tally > 3.0:
            champ_won_match += 1
        elif tally == 3.0:
            match_drawn += 1
    pchampwins_by_prob.append(champ_won_match/nr_trials)
    pchampdraws_by_prob.append(match_drawn/nr_trials)

import matplotlib.pyplot as plt

xt = plt.xticks([x for x in range(1,101) if x % 10 == 0])

plt.xlabel('Probability Percentage of Winning Single Game')
plt.ylabel('Probability of Winning/Drawing 6 Game Match')
#plt.xlim((0,100))
plt.plot(pchampwins_by_prob, 'b')
plt.plot(pchampdraws_by_prob, 'r--')
plt.legend(['Winning (variable x-axis)', 'Drawing (fixed at 0.1)'])
plt.show()
