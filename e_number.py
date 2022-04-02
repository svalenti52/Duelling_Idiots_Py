# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:14:25 2022

@author: svale
"""

# e_number.py

import random as rd

N = 100000
bin_width = 1/N

random_results = [rd.random() for x in range(N)]

bins_right_edge = [bin_width + x*bin_width for x in range(N)]

bin_counts = [0 for x in range(N)]

print(bins_right_edge[9999])

for x in random_results:
    for ix, bin_re in enumerate(bins_right_edge):
        if x < bin_re:
            bin_counts[ix] += 1
            break

count_bin_zeros = bin_counts.count(0)

print(count_bin_zeros)
print('approximation of e = ', N / count_bin_zeros)
