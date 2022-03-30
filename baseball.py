# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 07:48:31 2022

@author: svale
"""

# baseball.py

import random as rd

stronger_team = [x / 100.0 for x in range(51, 101)]

nr_trials = 100000

wt_graph = []
series_len_4 = []
series_len_5 = []
series_len_6 = []
series_len_7 = []

for st in stronger_team:
    series_length_4 = 0
    series_length_5 = 0
    series_length_6 = 0
    series_length_7 = 0
    weaker_team_total = 0
    for ix in range(nr_trials):
        stronger_team_wins = 0
        weaker_team_wins = 0
        while stronger_team_wins < 4 and weaker_team_wins < 4:
            if rd.random() <= st:
                stronger_team_wins += 1
            else:
                weaker_team_wins += 1
        if weaker_team_wins == 4:
            weaker_team_total += 1
        series_length = stronger_team_wins + weaker_team_wins
        if series_length == 4:
            series_length_4 += 1
        elif series_length == 5:
            series_length_5 += 1
        elif series_length == 6:
            series_length_6 += 1
        elif series_length == 7:
            series_length_7 += 1
    
    wtw_prob = weaker_team_total / nr_trials
    wt_graph.append(wtw_prob)
    series_len_4.append(series_length_4 / nr_trials)
    series_len_5.append(series_length_5 / nr_trials)
    series_len_6.append(series_length_6 / nr_trials)
    series_len_7.append(series_length_7 / nr_trials)

import matplotlib.pyplot as plt
x_axis = [x for x in range(51,101)]
xtk = [x for x in range(101) if x % 10 == 0]
xt = plt.xticks([x for x in xtk])
yt = plt.yticks([x / 10 for x in range(101)])

plt.xlabel('Percentage Probability for Stronger Team')
plt.ylabel('Prob of Weaker Team Winning, Series Length')
#plt.xlim((0,50))
plt.plot(x_axis, wt_graph, 'y')
plt.plot(x_axis, series_len_4, 'b')
plt.plot(x_axis, series_len_5, 'g')
plt.plot(x_axis, series_len_6, 'c')
plt.plot(x_axis, series_len_7, 'r')
plt.legend(['Weaker Team Wins Series', '4 Game Series', '5 Game Series', '6 Game Series', '7 Game Series'])
plt.show()
