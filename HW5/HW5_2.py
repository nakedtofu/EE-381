# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 06:47:26 2018

@author: NAO
"""

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import math

def HW5_2(dof):
    y = 0
    for i in range(dof):
        y = y + pow( np.random.standard_normal(100), 2)
    x = np.linspace (-1, 30, 100)
    #y = chi2.pdf(x, dof)
    plt.plot(x, y, label = ('dof:', dof))
    plt.legend()
    plt.title('Chi2')
    plt.xlabel('x value')
    plt.ylabel('y value')
    
HW5_2(1)
HW5_2(10)
plt.show()