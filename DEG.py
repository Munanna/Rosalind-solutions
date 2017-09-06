# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:55:35 2017

@author: OMNISLO
"""

f = open('rosalind_deg.txt', 'r')
vertices = []
for line in f.readlines()[1:]:
    l = line.strip('\n')
    for num in l.split(' '):
        vertices.append(int(num))
f.close()
nf = open('deg_answer.txt', 'w+')
    
edges = {}
for e in range(max(vertices)+1):
    edges[e] = 0
del edges[0]
    
for v in vertices:
    edges[v] += 1

for e in edges:
    nf.write(str(edges[e]) + ' ')
nf.close()



