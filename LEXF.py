# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:26:07 2017

@author: OMNISLO
"""

f = open('rosalind_lexf.txt', 'r')
lines = f.readlines()
f.close()

letters = lines[0].strip('\n').split(' ')
num = int(lines[1])


def kmers (letterlist, number):
    if number == 1:
        return letterlist
    else: 
        newlist = []
        for l in kmers(letterlist, number-1):
            for e in letterlist:
                n = l+e
                newlist.append(n)
        return newlist
                
kmerlist = kmers(letters, num)

nf = open('lexf_answer.txt', 'w+')
for k in kmerlist:
    nf.write(k)
    nf.write('\n')
nf.close()
