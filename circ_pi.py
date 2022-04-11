# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:23:18 2022

@author: svale
"""

# circ_pi.py

import random as rd

nr_trials = 100000

a = [x/100 for x in range(101)]

No_Ends = []
One_End = []
Two_Ends = []

nr_no_end = 0
nr_one_end = 0
nr_two_ends = 0

x = rd.random()
y = rd.random()

for A in a:
    nr_no_end = 0
    nr_one_end = 0
    nr_two_ends = 0

    for ix in range(nr_trials):
    
        while x**2 + y**2 >= 1:
            x = rd.random()
            y = rd.random()
        
        if (x+A)**2 + y**2 < 1:
            nr_no_end += 1
        elif (x-A)**2 + y**2 >= 1:
            nr_two_ends += 1
        else:
            nr_one_end += 1
        
        x = rd.random()
        y = rd.random()

    No_Ends.append(nr_no_end/nr_trials)
    One_End.append(nr_one_end/nr_trials)
    Two_Ends.append(nr_two_ends/nr_trials)
#print('No ends = ', nr_no_end / nr_trials)
#print('One end = ', nr_one_end / nr_trials)
#print('Two ends = ', nr_two_ends / nr_trials)

import matplotlib.pyplot as plt
#xtk = [x for x in range(101) if x % 10 == 0]
#xt = plt.xticks([x for x in xtk])
# yt = plt.yticks([x / 10 for x in range(101)])

plt.xlabel('Percentage Probability for Stronger Team')
plt.ylabel('Prob of Weaker Team Winning, Series Length')
#plt.xlim((0,50))
plt.plot(No_Ends, 'r')
plt.plot(One_End, 'b')
plt.plot(Two_Ends, 'g')

plt.legend(['No Ends Over Edge', 'One End Over Edge', 'Two Ends Over Edge'])
plt.show()
