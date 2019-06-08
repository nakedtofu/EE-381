# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:36:19 2018

@author: NAO
"""

import random as rand

def die_throw(number, throw_count):
    
    results = []
    
    for i in range(0,throw_count):
        results.append(rand.randint(1, 6))
        
    print("1 has shown up", results.count(1),
          "times out of", throw_count, "throws.")
    print("Percentage:", round(results.count(1)/throw_count, 4),
          "( probability of getting a 1 is", round(1/6, 4), ")")
    
die_throw(1,10)
die_throw(1,100)
die_throw(1,1000)
die_throw(1,10000)
