# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:34:18 2017

@author: OMNISLO
"""
dna_seq = ''
f = open('rosalind_ini.txt', 'r')
for line in f.readlines():
    line = line.strip('/n')
    dna_seq += line
f.close()

from Bio.Seq import Seq
my_seq = Seq(dna_seq)
print(str(my_seq.count("A")) + ' ' + str(my_seq.count("C")) + ' ' + str(my_seq.count("G")) + ' ' + str(my_seq.count("T")))