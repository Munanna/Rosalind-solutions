# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 21:27:48 2017

@author: OMNISLO
"""
f = open('rosalind_bins.txt', 'r')
lines = f.readlines()
f.close()

data = []
numbers = []
search = []

for d in lines:
    d = d.strip('\n')
    data.append(d)

for n in data[2].split(' '):
    m = int(n)
    numbers.append(m)

for n in data[3].split(' '):
    m= int(n)
    search.append(m)

newfile = open('bins_answer.txt', 'w+')

for e in search:
    if e in numbers:
        newfile.write(str(numbers.index(e) + 1))
        newfile.write(' ')
    else:
        newfile.write(str(-1))
        newfile.write(' ')
        
newfile.close()