# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 00:51:51 2017

@author: OMNISLO
"""

f = open('rosalind_splc.txt', 'r')
seqs = []
l = ''
counter=0
for line in f.readlines():
    if line[0] != '>':
        l += line.strip('\n')
    else:
        seqs.append(l)
        l = ''
        counter +=1
seqs.append(l)
f.close()
seqs.remove('')

full_sequence = seqs[0]
introns = seqs[1:]

sequence = full_sequence
for i in introns:
    sequence = sequence.replace(i, '')

dna_codons = {' ':['TAA','TAG','TGA'], 'F':['TTT','TTC'], 'S':['TCT','TCG','TCC','TCA','AGT','AGC'], 'Y':['TAT','TAC'], 'C':['TGT','TGC'], 'W' : ['TGG'], 'L':['TTA','TTG','CTT','CTA','CTC','CTG'], 'P':['CCT','CCC','CCG','CCA'], 'R':['CGT','CGC','CGG','CGA','AGA','AGG' ], 'H':['CAT', 'CAC'], 'Q':['CAA','CAG'], 'I':['ATT','ATC','ATA'], 'M':['ATG'], 'T':['ACT','ACC','ACA','ACG'], 'N':['AAT','AAC'], 'K':['AAA','AAG'], 'V':['GTT','GTC','GTA','GTG'], 'A':['GCT','GCC','GCG','GCA'], 'D':['GAT','GAC'], 'E':['GAA','GAG'], 'G':['GGT','GGC','GGA','GGG']}

protein = '' 
counter = 0
while counter <= len(sequence):
    codon = sequence[counter:counter+3]
    for c in dna_codons:
        if codon in dna_codons[c]:
            protein += c
    counter += 3

print (protein)