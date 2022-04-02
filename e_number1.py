# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 07:27:46 2022

@author: svale
"""

import random as rd

nr_trials = 100000

nr_right_edges = 10

domain = 500

sums = []

for ix in range(nr_trials):
    right_edge = [1.0]
    for jx in range(nr_right_edges):
        right_edge.append(rd.random() * right_edge[jx])
        right_edge_ = right_edge[1::]
        sum_list = sum(right_edge_)
    sums.append(sum_list)

sorted_sums = sorted(sums)

graph_results = []

for ix in range(domain):
    nr_lt = 0
    for jx in range(nr_trials):
        if sorted_sums[jx] < ix / 100.0:
            nr_lt += 1
    graph_results.append(nr_lt / nr_trials)

import matplotlib.pyplot as plt

xt = plt.xticks([x for x in range(domain+1) if x % (domain//10) == 0])
# yt = plt.yticks([x for x in range()])

#bottom, top = plt.ylim((0, N))
plt.xlabel('Thickness Multiplied by 100')
plt.ylabel('Probability Less Than Thickness')
#plt.xlim((0,100))
plt.plot(graph_results, 'b')
plt.show()

print(graph_results[100]) # e**-gamma
