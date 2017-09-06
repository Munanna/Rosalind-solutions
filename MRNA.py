# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:14:33 2017

@author: OMNISLO
"""
f = open('rosalind_mrna.txt', 'r')
protein = f.read() + ' '
f.close()

rna_codons = {' ':['UAA','UAG','UGA'], 'F':['UUU','UUC'], 'S':['UCU','UCG','UCC','UCA','AGU','AGC'], 'Y':['UAU','UAC'], 'C':['UGU','UGC'], 'W' : ['UGG'], 'L':['UUA','UUG','CUU','CUA','CUC','CUG'], 'P':['CCU','CCC','CCG','CCA'], 'R':['CGU','CGC','CGG','CGA','AGA','AGG' ], 'H':['CAU', 'CAC'], 'Q':['CAA','CAG'], 'I':['AUU','AUC','AUA'], 'M':['AUG'], 'T':['ACU','ACC','ACA','ACG'], 'N':['AAU','AAC'], 'K':['AAA','AAG'], 'V':['GUU','GUC','GUA','GUG'], 'A':['GCU','GCC','GCG','GCA'], 'D':['GAU','GAC'], 'E':['GAA','GAG'], 'G':['GGU','GGC','GGA','GGG']}

possibilities = 1
for a in protein:
    for c in rna_codons:
        if c == a:
            possibilities *= len(rna_codons[c]) 

print (possibilities % 1000000)