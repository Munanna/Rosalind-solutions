# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:33:55 2017

@author: OMNISLO
"""
f = open('rosalind_iev.txt', 'r')
pairstring = f.read()
pairlist = pairstring.split(' ')
pairs = []
for p in pairlist:
    pairs.append(int(p))


dominant_phenotype = pairs[0]*2*1+pairs[1]*2*1+pairs[2]*2*1+pairs[3]*2*0.75+pairs[4]*2*0.5
print (dominant_phenotype)