# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:26:16 2017

@author: OMNISLO
"""

def gc_count(string_list):
    gc_counter = 0
    length = 0
    for x in string_list:
        for char in x:
            if char == 'C' or char == 'G':  
                gc_counter += 1
        length += len(x)
    result = (gc_counter/length)*100
    return round(result, 6)

f = open('rosalind_gc.txt')
lines = f.readlines()
f.close()

seqs = {}
for l in lines:
    l = l.strip('\n')
    l = l.strip('>')
    if l[0:8] == 'Rosalind':
        d=l
        seqs[d] = []
    else:
        seqs[d].append(l)

content = {}
for d in seqs:
    result = gc_count(seqs[d])
    content[d] = result

max_value = 0
max_name = ''

for d in content:
    if content[d]>max_value:
        max_value = content[d]
        max_name = d

print (d)
print (max_value)
