# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 18:50:12 2017

@author: OMNISLO
"""

seq = "GATATATGCATATACTT"
substring = "ATAT"
l = len(substring)

counter = 0
for s in seq[:-l]:
    if seq[counter:counter+l] == substring:
        print (counter+1)
    counter += 1