# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 00:53:08 2017

@author: OMNISLO
"""

f = open('rosalind_maj.txt', 'r')
lines = f.readlines()
f.close()

lists = []

for l in lines:
    l = l.strip('\n')
    l = l.split(' ')
    nums = []
    for e in l:
        e = int(e)
        nums.append(e)
    lists.append(nums)
    
n = lists[0][1]
lists = lists[1:]
values = []

for l in lists:
    dictionary = {}
    for e in l:
        if e not in dictionary:
            dictionary[e] = 1
        else:
            dictionary[e] += 1
    counter = 0
    for v in dictionary:
        if dictionary[v] > (n/2):
            values.append(v)
            counter += 1
    if counter == 0:
        values.append(-1)
        
newfile = open('maj_answer.txt', 'w+')

for e in values:
    newfile.write(str(e))
    newfile.write(' ')
newfile.close()
