# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

def heightSeparator(y1, y2):  
    
    data_min = y1[1]
    data_max = y1[1]
    
    for i in range(len(y1)):
        if(y1[i] < data_min):
            data_min = y1[i]
        if(y1[i] > data_max):
            data_max = y1[i]
            
    for j in range(len(y2)):
        if(y2[j] < data_min):
            data_min = y2[j]
        if(y2[j] > data_max):
            data_max = y2[j] 
            
    step = (data_max - data_min) / 5
    bin_range = [data_min, data_min + step, data_min + 2 * step,
                 data_min + 3 * step, data_min + 4 * step, data_max]
    
    plt.hist([y1,y2], histtype='bar', bins = bin_range,
             color = ['r', 'b'], label=['Boys', 'Girls'])
    plt.xticks(bin_range)
    plt.legend()
    plt.title('Height of Students')
    plt.xlabel('Height range')
    plt.ylabel('Number of students')
    plt.show()

Boys = [65, 67, 72.5, 71, 82, 59, 62, 63.4, 66, 65, 73, 71, 72]
Girls = [58, 56.5, 54, 60, 62, 59, 60.5, 61, 63, 65, 66, 61.5, 62.5]

heightSeparator(Boys, Girls)