# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 03:23:32 2018

@author: NAO
"""

import matplotlib.pyplot as plt
import numpy as np

def HW6(sample_size, sampling):
    
    list_numbers = []
    ave_numbers = []
    
    for i in range(sample_size):
        list_numbers = []
        for k in range(sampling):
            list_numbers.append(np.random.exponential(sampling))
        ave_numbers.append(np.mean(list_numbers))
    
    mean = np.mean(ave_numbers)
    std = np.std(ave_numbers)
    
    print('')
    print('printing histogram of', sampling, 'number sampling')
    
    #plot histogram    
    plt.hist(ave_numbers, histtype='bar', bins = 10,
             color = ['r'], label=['Numbers'])
    plt.legend()
    plt.title('Central Limit Theorem')
    plt.xlabel('Value')
    plt.ylabel('Amount of Numbers')
    
    plt.show()
    
    print('mean =', mean)
    print('standard deviation =', std)

sample_size = 2000
sampling = 2
HW6(sample_size, sampling)
sampling = 5
HW6(sample_size, sampling)
sampling = 30
HW6(sample_size, sampling)