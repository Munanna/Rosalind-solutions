# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 01:14:50 2017

@author: OMNISLO
"""

f = open('rosalind_ddeg.txt', 'r')
lines = f.readlines()
num_vertices = int(lines[0].split(' ')[0])
vertices = []
for line in lines[1:]:
    l = line.strip('\n')
    for num in l.split(' '):
        vertices.append(int(num))
f.close()

deg = {}
for e in range(num_vertices+1):
    deg[e] = 0
del deg[0]


for v in vertices:
    deg[v] += 1

neighbours = {}
counter = 0
while counter < len(vertices):
    if vertices[counter] not in neighbours:
        neighbours[vertices[counter]]=[]
    if vertices[counter+1] not in neighbours:
        neighbours[vertices[counter+1]]=[]    
    neighbours[vertices[counter]].append(vertices[counter+1])
    neighbours[vertices[counter+1]].append(vertices[counter])
    counter += 2

ddeg = {}
for e in range(num_vertices+1):
    ddeg[e] = 0
del ddeg[0]    

for e in neighbours:
    for l in neighbours[e]:
        ddeg[e] += deg[l]

nf = open('ddeg_answer.txt', 'w+')
for e in ddeg:
    nf.write(str(ddeg[e]) + ' ')
nf.close()
