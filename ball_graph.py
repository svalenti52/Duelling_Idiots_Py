# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 08:14:37 2022

@author: svale
"""

import pandas as pd

graf = open('c:/cygwin64/home/svale/graph/ball.txt')

bg = pd.Series(graf)

print(bg)

print(bg[9])

import matplotlib.pyplot as plt

#ax1 = plt.axis()
#ax1.Axis.set_inverted()
xt = plt.xticks([0, 200, 400, 600, 800, 1000])
yt = plt.yticks([35, 30, 25, 20, 15, 10, 5, 0])
#print(xt)
bottom, top = plt.ylim((35, 0))
plt.xlabel('Number of Selections')
plt.ylabel('Black Balls in Urn')
plt.xlim((0,1000))
plt.plot(bg, 'b')
plt.show()
#print(bottom, top)
