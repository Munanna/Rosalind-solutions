# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:39:35 2017

@author: OMNISLO
"""

a=100
b=200

counter=0

for x in range (a,b+1):
    if x % 2 == 1:
        counter += x
        
print (counter)
