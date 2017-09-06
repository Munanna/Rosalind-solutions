# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:59:19 2017

@author: OMNISLO
"""
f = open('rosalind_prot.txt')
s = f.read()
f.close()

rna_codons = {'':['UAA','UAG','UGA'], 'F':['UUU','UUC'], 'S':['UCU','UCG','UCC','UCA','AGU','AGC'], 'Y':['UAU','UAC'], 'C':['UGU','UGC'], 'W' : ['UGG'], 'L':['UUA','UUG','CUU','CUA','CUC','CUG'], 'P':['CCU','CCC','CCG','CCA'], 'R':['CGU','CGC','CGG','CGA','AGA','AGG' ], 'H':['CAU', 'CAC'], 'Q':['CAA','CAG'], 'I':['AUU','AUC','AUA'], 'M':['AUG'], 'T':['ACU','ACC','ACA','ACG'], 'N':['AAU','AAC'], 'K':['AAA','AAG'], 'V':['GUU','GUC','GUA','GUG'], 'A':['GCU','GCC','GCG','GCA'], 'D':['GAU','GAC'], 'E':['GAA','GAG'], 'G':['GGU','GGC','GGA','GGG']}

rna = ''
counter = 0

while counter <= len(s):
    codon = (s[counter:counter+3])
    for d in rna_codons:
        if codon in rna_codons[d]:
            rna += d
    counter += 3


print (rna)