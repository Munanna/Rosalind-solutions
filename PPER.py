# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 01:42:21 2017

@author: OMNISLO
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 
    
n = 96
k = 9

partial_permutations=factorial(n)/factorial(n-k)
print(partial_permutations%1000000)
