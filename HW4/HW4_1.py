# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:50:21 2018

@author: NAO
"""

import scipy.stats as ss

def HW4_1(n, p, k):
    y = ss.binom.cdf(k,n,p)
    print("Probability of getting less than 3 times of '5' out of 8 throws:", y)
    
n = 8
p = 1/6
k = 3

HW4_1(n, p, k)