# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:42:06 2017

@author: OMNISLO
"""

dna_seq = "GATGGAACTTGACTACGTAAATT"

rna_seq = ""

for x in dna_seq:
    if x=="T":
        rna_seq += "U"
    else:
        rna_seq += x

print (rna_seq)
