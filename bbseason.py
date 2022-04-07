# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 09:11:18 2022

@author: svale
"""

# bbseason.py

import random as rd
import numpy as np
import math as m

resolution = 100

def P(n, p):
    return n * p

def binomial_calc(n, k, p):
    bi_sum = 0.0
    for kx in range(k,n+1):
        bc = m.comb(n, kx)
        bi_sum = bi_sum + bc * p**kx * (1.0-p)**(n-kx)
    return bi_sum

P81 = [P(81, x/resolution) for x in range(resolution+1)]
P81 = P81[1::]
P162 = [P(162, x/resolution) for x in range(resolution+1)]
P162 = P162[1::]

P81c = [int(np.ceil(x)) for x in P81]
P162c = [int(np.ceil(x)) for x in P162]

print(P81c[0])
P81s = [binomial_calc(81, P81c[k-1], k/resolution) for k in range(1,resolution+1)]
P162s = [binomial_calc(162, P162c[k-1], k/resolution) for k in range(1,resolution+1)]

R = [x/y for (x,y) in zip(P81s, P162s)]

import matplotlib.pyplot as plt

xt = plt.xticks([x for x in range(1,resolution+1) if x % (resolution/10) == 0])

plt.xlabel('Probability Percentage of Winning Single Game')
plt.ylabel('Ratio of Probabilities of Winning At Least np Games')
#plt.xlim((0,100))
plt.plot(R, 'b')
plt.show()
