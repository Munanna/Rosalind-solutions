# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:03:05 2017

@author: OMNISLO
"""

f = open('Downloads/rosalind_ini5.txt')

lines = f.readlines()
counter = 1

for line in lines:
    if counter % 2 == 0:
        print (line.strip('\n'))
    counter +=1