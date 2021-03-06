# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 00:41:20 2017

@author: OMNISLO
"""
matrix=[]

f = open('rosalind_cons.txt', 'r')
l = ''
counter1=0
for line in f.readlines():
    if line[0] != '>':
        l += line.strip('\n')
    else:
        matrix.append(l)
        l = ''
        counter1 +=1
matrix.append(l)
f.close()
matrix.remove('')

A = []
C = []
G = []
T = []
consensus = ""

for e in range(len(matrix[0])):
    a_counter = 0
    c_counter = 0
    g_counter = 0
    t_counter = 0
    for s in matrix:
        if s[e] == 'A':
            a_counter += 1
        if s[e] == 'C':
            c_counter += 1
        if s[e] == 'G':
            g_counter += 1
        if s[e] == 'T':
            t_counter += 1
    A.append(a_counter)
    C.append(c_counter)
    G.append(g_counter)
    T.append(t_counter)
    maximum = max(A[e], C[e], G[e], T[e])
    counter = 0
    if maximum == A[e]:
        consensus += "A"
        counter += 1
    if maximum == C[e] and counter == 0:
        consensus += "C"
        counter += 1
    if maximum == G[e] and counter == 0:
        consensus += "G"
        counter += 1
    if maximum == T[e] and counter == 0:
        consensus += "T"
        counter += 1


newfile = open('cons_answer.txt', 'w+')

newfile.write(consensus+'\n')
newfile.write("A: ")
for e in A:
    newfile.write(str(e)+' ')
newfile.write('\n')
newfile.write("C: ")
for e in C:
    newfile.write(str(e)+' ')
newfile.write('\n')
newfile.write("G: ")
for e in G:
    newfile.write(str(e)+' ')
newfile.write('\n')
newfile.write("T: ")
for e in T:
    newfile.write(str(e)+' ')
newfile.write('\n')

newfile.close()