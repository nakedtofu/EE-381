# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:55:00 2018

@author: NAO
"""

import random as rand
import matplotlib.pyplot as plt
import math

def HW4_2(min_v, max_v):
    
    numbers = []
    total = 0
    
    for x in range(2000):
        numbers.append(rand.randrange(min_v, max_v + 1))
        
    for a in range(len(numbers)):
       total = total + numbers[a]
       
    mean = total / 2000
    print('mean:', mean)
    
    prob = 1/(max_v - min_v + 1)
    
    possible_out = []
    possible_out.append(numbers[0])
    for v in range(len(numbers)):
        overlap = 0
        for d in range(len(possible_out)):
            if(numbers[v] == possible_out[d]):
                overlap = 1
        if(overlap == 0):
            possible_out.append(numbers[v])
            
    var = 0
            
    for s in possible_out:
        var = var + possible_out[s] * possible_out[s] * prob

    print('varience:', var)
    
    std = math.sqrt(var)
    
    print('standard deviation:', std)
    
    #plot histogram
    step = (abs(max_v) + abs(min_v)) / 4
    bin_range = [min_v, min_v + step, min_v + 2 *step, min_v + 3*step, max_v]
    
    plt.hist([numbers], histtype='bar', bins = 10,
             color = ['r'], label=['Numbers'])
    plt.xticks(bin_range)
    plt.legend()
    plt.title('-1 to 1 Probability Histogram')
    plt.xlabel('Value')
    plt.ylabel('Amount of Numbers')
    plt.show()

min_v = -1
max_v = 1    
HW4_2(min_v, max_v)