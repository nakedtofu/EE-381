# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 13:09:37 2018

@author: NAO
"""

from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt

def HW5_1(alpha, beta):
    x = np.linspace (0, 50, 1000)
    y = gamma.pdf(x, alpha, 1/beta) #theta = 1/beta
    plt.plot(x, y, label = (alpha, beta))
    plt.legend()
    plt.title('Gamma Distribution pdf')
    plt.xlabel('x value')
    plt.ylabel('y value')
    
HW5_1(1, 1)
HW5_1(1, 5)
HW5_1(1, 10)
HW5_1(5, 1)
HW5_1(10, 1)
HW5_1(10, 2)

plt.show()