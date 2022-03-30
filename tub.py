# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:45:39 2022

@author: svale
"""

# tub.py

ps = 0.2

N = 13

# probability profile as a function of N (number of ships)

def calc_ship_prof():
    snf = 1.0 - ps
    sf_list = []
    for ns in range(N+1):
        snf_t = 1.0
        for i in range(1, ns+1):
            snf_t *= snf
        sf_list.append(1.0 - snf_t)
    return sf_list

ships_north_prof = calc_ship_prof()
ships_south_prof_rev = [x for x in reversed(ships_north_prof)]
ships_prof = [x for x in zip(ships_north_prof, ships_south_prof_rev)]
print(ships_prof)

######################################

isl_north_prob = [x/100.0 for x in range(101)]
isl_south_prob_rev = [x for x in reversed(isl_north_prob)]
isl_prof = [x for x in zip(isl_north_prob, isl_south_prob_rev)]
print(isl_prof)

######################################

max_profile = []
for isl_prob in isl_prof:
    select_profile = []
    for i, sp in enumerate(ships_prof):
        north = sp[0] * isl_prob[0]
        south = sp[1] * isl_prob[1]
        select_profile.append((north + south, i))
    max_ship = max(select_profile)
    max_profile.append(max_ship[1])
print(max_profile)

######################################

import matplotlib.pyplot as plt

xt = plt.xticks([x for x in range(101) if x % 10 == 0])
yt = plt.yticks([x for x in range(N+1)])

bottom, top = plt.ylim((0, N))
plt.xlabel('Percentage Probabilty Ship is at Island 1')
plt.ylabel('Number Northern Tubs')
plt.xlim((0,100))
plt.plot(max_profile, 'b')
plt.show()
