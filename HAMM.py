# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:37:24 2017

@author: OMNISLO
"""

f = open('rosalind_hamm.txt')

lines = []
for x in f.readlines():
    x = x.strip('\n')
    lines.append(x)

counter = 0
mutationcounter = 0

for x in lines[0]:
    if x != lines[1][counter]:
        mutationcounter +=1
    counter +=1

print (mutationcounter)