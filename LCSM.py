# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:26:38 2017

@author: OMNISLO
"""
seqs=[]

f = open('rosalind_lcsm.txt', 'r')
l = ''
counter1=0
for line in f.readlines():
    if line[0] != '>':
        l += line.strip('\n')
    else:
        seqs.append(l)
        l = ''
        counter1 +=1
seqs.append(l)
f.close()
seqs.remove('')
minseq = min(seqs, key=len)


def substrings(string, length):
    counter = 0
    substrings = []
    for s in string[:-length+1]:
        substring = string[counter:counter+length]
        substrings.append(substring)
        counter += 1
    return (substrings)
    
nf = open('lcsm_motifs.txt', 'w+')
for e in range(len(minseq)+1):
    motifs = []
    substringlist = substrings(minseq, e)
    for x in substringlist:
        if x not in motifs:
            motifs.append(x)
            nf.write(x + '\n')
motifs = []
nf.close()

mf = open('lcsm_motifs.txt', 'r')
for line in mf.readlines()[::-1]:
    counter = 0
    line = line.strip('\n')
    for seq in seqs:
        if line in seq:
            counter += 1     
    if counter == len(seqs):
        print (line)
        break

mf.close()

