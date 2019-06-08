# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:08:06 2018

@author: NAO
"""

import numpy as np
import matplotlib.pyplot as plt

def HW3_1(x, y):

   a1 = ( len(x) * sum(x * y) - (sum(x) * sum(y)) ) / ( len(x) * sum(x * x) - sum(x) * sum(x) ) 
   
   b1 = ( sum(y) * sum(x * x) - sum(x) * sum(x * y) ) / ( len(y) * sum(x * x) - sum(x) * sum(x) )
   
   plt.plot(x, a1 * x + b1, 'b', label = 'fitting')
   plt.plot(x, y, 'ro', label = 'data')
   plt.axis([0, 9, -2, 2])
   plt.show()
   
   
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([0, .8, .9, .1, -.8, -1, -1.2, -1.6, -1.9])

HW3_1(x, y);