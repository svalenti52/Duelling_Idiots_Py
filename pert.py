# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:59:56 2022

@author: svale
"""

# pert.py

import random as rd

task1 = 0
task2 = 1
task3 = 2
task4 = 3
task5 = 4
task6 = 5
task7 = 6
task8 = 7

work = 0
es = 1
ef = 2
ls = 3
lf = 4
nt = 5
pt = 6
rndwrk = 7

nr_events = 1

tasks = [[[0,0], 0, 0, 0, 0, [task2,task3], [], 0],
         [[2,4], 0, 0, 0, 0, [task4,task5], [task1], 0],
         [[1,2], 0, 0, 0, 0, [task4,task5], [task1], 0],
         [[1,2], 0, 0, 0, 0, [task6], [task2,task3], 0],
         [[2,4], 0, 0, 0, 0, [task7], [task2,task3], 0],
         [[2,4], 0, 0, 0, 0, [task7], [task4], 0],
         [[1,2], 0, 0, 0, 0, [task8], [task5,task6], 0],
         [[0,0], 0, 0, 0, 0, [], [task7], 0]]

rev_tasks = reversed(tasks)

completion = []
critical = [0 for x in range(9)]

for ne in range(nr_events):
    for task in tasks:
        task[rndwrk] = rd.randint(task[work][0], task[work][1])
        task[ef] = task[rndwrk] + task[es]
        for tx in task[nt]:
            if task[ef] > tasks[tx][es]:
                tasks[tx][es] = task[ef]
        if task[nt] == []:
            task[lf] = task[ef]
    
    for rtask in rev_tasks:
        rtask[ls] = rtask[lf] - rtask[rndwrk]
        for rtx in rtask[pt]:
#            if task[ls] < tasks[rtx][lf]:
            tasks[rtx][lf] = rtask[ls]

    for ix, task in enumerate(tasks):
        if task[es] == task[ls]:
            critical[ix] += 1

    completion.append(tasks[task8][ef])
    
    # for task in tasks:
    #     task[es] = 0
    #     task[ef] = 0
    #     task[ls] = 0
    #     task[lf] = 0
    


#=============================================================================
print('1. ', tasks[task1])
print('2. ', tasks[task2])
print('3. ', tasks[task3])
print('4. ', tasks[task4])
print('5. ', tasks[task5])
print('6. ', tasks[task6])
print('7. ', tasks[task7])
print('8. ', tasks[task8])

#=============================================================================

import matplotlib.pyplot as plt
plt.xlabel('')
plt.ylabel('')

# To get distribution plot, change cumulative to True
#n, bins, patches = plt.hist(completion, 13, density=False, cumulative=False)
#n, bins, patches = plt.hist(critical, 16, density=False, cumulative=False)
plt.plot(critical)
plt.show()
