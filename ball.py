# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:36:29 2022

@author: svale
"""

# ball.py

import random as rd

NR_BALLS_IN_URN = 50
NR_TRIALS = 1000

org_black_urn = [True for i in range(NR_BALLS_IN_URN)]

org_white_urn = [False for i in range(NR_BALLS_IN_URN)]

graph = []

for exchange in range(NR_TRIALS):
    nr_black_balls_in_black_urn = org_black_urn.count(True)
    norm_0_1 = nr_black_balls_in_black_urn / NR_BALLS_IN_URN
    if exchange == 0:
        print(norm_0_1)
    graph.append(norm_0_1)
    black_index = rd.randint(0, NR_BALLS_IN_URN - 1)
    white_index = rd.randint(0, NR_BALLS_IN_URN - 1)
    from_black = org_black_urn[black_index]
    from_white = org_white_urn[white_index]
    # exchange
    org_black_urn[black_index] = from_white
    org_white_urn[white_index] = from_black

import matplotlib.pyplot as plt

xt = plt.xticks([0, NR_TRIALS])
yt = plt.yticks([0, 0.4, 0.5, 0.6, 1])

bottom, top = plt.ylim((0.30, 1))
plt.xlabel('Number of Selections')
plt.ylabel('Black Balls in Urn')
plt.xlim((0,NR_TRIALS))
plt.plot(graph, 'b')
plt.show()
