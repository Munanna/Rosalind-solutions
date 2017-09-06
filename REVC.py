# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:56:05 2017

@author: OMNISLO
"""

s = "AAAACCCGGT"

str = s[::-1]
revc=""

for e in str:
    if e=='A':
        revc += 'T'
    if e=='T':
        revc += 'A'
    if e=='C':
        revc += 'G'
    if e=='G':    
        revc += 'C'

print (revc)