# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:37:10 2017

@author: OMNISLO
"""

f = open('rosalind_orf.txt', 'r')
dna_seq = ''
counter=0
for line in f.readlines():
    if line[0] != '>':
        dna_seq += line.strip('\n')
f.close()

rna_seq = ""
for x in dna_seq:
    if x=="T":
        rna_seq += "U"
    else:
        rna_seq += x

rev_rna_seq = rna_seq[::-1]
revc_rna_seq=""
for e in rev_rna_seq:
    if e=='A':
        revc_rna_seq += 'U'
    if e=='U':
        revc_rna_seq += 'A'
    if e=='C':
        revc_rna_seq += 'G'
    if e=='G':    
        revc_rna_seq += 'C'
        
seqs = [rna_seq, revc_rna_seq]
allseqs = []
for s in seqs:
    allseqs.append(s)
    allseqs.append(s[1:])
    allseqs.append(s[2:])

rna_codons = {'/':['UAA','UAG','UGA'], 'F':['UUU','UUC'], 'S':['UCU','UCG','UCC','UCA','AGU','AGC'], 'Y':['UAU','UAC'], 'C':['UGU','UGC'], 'W' : ['UGG'], 'L':['UUA','UUG','CUU','CUA','CUC','CUG'], 'P':['CCU','CCC','CCG','CCA'], 'R':['CGU','CGC','CGG','CGA','AGA','AGG' ], 'H':['CAU', 'CAC'], 'Q':['CAA','CAG'], 'I':['AUU','AUC','AUA'], 'M':['AUG'], 'T':['ACU','ACC','ACA','ACG'], 'N':['AAU','AAC'], 'K':['AAA','AAG'], 'V':['GUU','GUC','GUA','GUG'], 'A':['GCU','GCC','GCG','GCA'], 'D':['GAU','GAC'], 'E':['GAA','GAG'], 'G':['GGU','GGC','GGA','GGG']}

prots=[]
for s in allseqs:
    counter = 0
    prot = ''
    while counter <= len(s):
        codon = s[counter:counter+3]
        for c in rna_codons:
            if codon in rna_codons[c]:
                prot += c
        counter += 3
    prots.append(prot)

possible = []
for p in prots:
    counter = 0
    for l in p:
        if l == 'M':
            protein = ''
            rem = (p[counter:])
            for x in rem:
                if x != '/':
                    protein += x
                else:
                    if protein not in possible:
                        possible.append(protein)
                    break
        counter +=1 

nf = open('orf_answer.txt', 'w+')

for p in possible:
    nf.write(p + '\n')
nf.close()