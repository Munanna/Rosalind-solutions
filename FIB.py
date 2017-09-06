# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 22:53:39 2017

@author: OMNISLO
"""

n=5
k=3


def Fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return Fib(n-1)+k*Fib(n-2)

print (Fib(n))
