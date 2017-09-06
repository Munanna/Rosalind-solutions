# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:01:47 2017

@author: OMNISLO
"""

import urllib.request

f = open('rosalind_mprt.txt', 'r')
accession = f.readlines()
f.close()

uniprot_ids = []
for a in accession:
    a = a.strip('\n')
    uniprot_ids.append(a)

seqs = {}
for uniprot_id in uniprot_ids:
    page = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + uniprot_id + ".fasta").read()
    seqs[uniprot_id] = str(page)

newfile = open('mprt_answer.txt', 'w+')
for s in seqs:
    ls = (seqs[s].split('\\n'))
    del(ls[0])
    seqs[s] = ''.join(ls)
    seqs[s] = seqs[s][:-1]
    print(s)
    print(seqs[s])
    counter = 0
    start_indices = []
    for x in seqs[s][:-3]:
        substring = seqs[s][counter:counter+4]
        if substring[0] == 'N' and substring[1] != 'P' and (substring[2] == 'S' or substring[2] == 'T') and substring[3] != 'P':
            print (substring)
            start_indices.append(counter+1)
        counter += 1
    print (start_indices)
    if start_indices != []:
        newfile.write(s+'\n')
        for x in start_indices:
            newfile.write(str(x)+' ')
        newfile.write('\n')


