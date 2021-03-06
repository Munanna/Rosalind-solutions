# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 01:17:26 2017

@author: OMNISLO
"""

f = open('rosalind_tran.txt', 'r')

sequences = []
string = ''
for line in f.readlines():
    if line[0] == '>':
        if string != '':
            sequences.append(string)
        string = ''
    else:
        line = line.strip('\n')
        string += line
sequences.append(string)
f.close()

template = sequences[0]
copy = sequences[1]

purines = ['A', 'G']
pyrimidines = ['C', 'T']


counter = 0
transitioncounter = 0
transversioncounter = 0

for t in template:
    c = copy[counter]
    if t != c:
        if (t in purines and c in purines) or (t in pyrimidines and c in pyrimidines):
            transitioncounter += 1
        else:
            transversioncounter += 1
    counter += 1

R = transitioncounter/transversioncounter
print (round(R, 11))
