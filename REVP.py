# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:41:25 2017

@author: OMNISLO
"""

f = open('rosalind_revp.txt', 'r')
dna_seq = ''
counter=0
for line in f.readlines():
    if line[0] != '>':
        dna_seq += line.strip('\n')
f.close()

def revc(seq):
    cdna_seq=""

    for e in seq:
        if e=='A':
            cdna_seq += 'T'
        if e=='T':
            cdna_seq += 'A'
        if e=='C':
            cdna_seq += 'G'
        if e=='G':    
            cdna_seq += 'C'
    
    rev_cdna_seq=cdna_seq[::-1]

    return rev_cdna_seq

length = 4
while length <= 12:
    counter = 0
    while counter <= (len(dna_seq) - length):
        sequence = dna_seq[counter:counter+length]
        if sequence == revc(sequence):
            print (counter+1, len(sequence))
        counter += 1
    length += 1
    
    