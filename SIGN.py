# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:38:36 2017

@author: OMNISLO
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 

def numbers(n):
    numlist = []
    for i in range(n+1):
        if i > 0:
            numlist.append(i)
    return (numlist)
                 

def permutations(numlist):
    if len(numlist)==1:
        return numlist[0]
    if len(numlist)==2:
        return [numlist, numlist[::-1]]
    if len(numlist) >= 3:
        permlist = []
        for num in numlist:
            first = num
            numlist2 = numlist[:]
            numlist2.remove(num)
            permlist2 = permutations(numlist2)
            for p in permlist2:
                p.insert(0, first)
                permlist.append(p)
        return permlist

def sign(numbers):
    if len(numbers)==1:
        l1 = []
        l2 = []
        l3 = []
        n = numbers[0]
        m = n*(-1)
        l1.append(n)
        l2.append(m)
        l3.append(l1)
        l3.append(l2)
        return (l3)
    if len(numbers)>=2:
        signlist = []
        n = numbers[0]
        m = n*(-1)
        l1 = numbers[:]
        l1.remove(n)
        l2 = sign(l1)
        for i in l2:
            i.insert(0, n)
            signlist.append(i[:])
            i.remove(n)
            i.insert(0, m)
            signlist.append(i[:])
            i.remove(m)
        return signlist

m = 3
number = factorial(m)*2**m

nf = open('sign_answer.txt', 'w+')

nf.write(str(number))
nf.write('\n')

permutations_list = (permutations(numbers(m)))
for p in permutations_list:
    signed_permutations = sign(p)
    for sp in signed_permutations:
        for i in sp:
            nf.write(str(i))
            nf.write(' ')
        nf.write('\n')

nf.close()
