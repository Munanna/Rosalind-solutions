# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 00:48:02 2017

@author: OMNISLO
"""

seqs={}

f = open('rosalind_grph.txt', 'r')
for line in f.readlines():
    if line[0] == '>':
        d = line[1:].strip('\n')
        seqs[d] = ''
    else:
        line = line.strip('\n')
        seqs[d] += line
f.close()

newfile = open('grph_answer.txt', 'w+')

for e in seqs:
    for s in seqs:
        if seqs[s][-3:] == seqs[e][0:3] and e != s:
            newfile.write(s+' '+e+'\n')

newfile.close()