# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:17:58 2017

@author: OMNISLO
"""

k=2
m=2
n=2
total=k+m+n

prob_kk = (k/total)*((k-1)/(total-1))
prob_km = (k/total)*(m/(total-1)) + (m/total)*(k/(total-1))
prob_kn = (k/total)*(n/(total-1)) + (n/total)*(k/(total-1))
prob_mm = (m/total)*((m-1)/(total-1))
prob_mn = (m/total)*(n/(total-1)) + (n/total)*(m/(total-1))
prob_nn = (n/total)*((n-1)/(total-1))

probability = prob_kk+prob_km+prob_kn+prob_mm*0.75+prob_mn*0.5

print (round(probability,5))