# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:06:45 2018

@author: NAO
"""

import scipy.stats as ss
import numpy as np

pdf = []

def HW4_3(pieces, defect_p):
    
    for i in range(pieces + 1):
       pdf.append(ss.binom.pmf(i, pieces, defect_p))
       print(i, "defects: ", pdf[i]*100, "%")
       
    print("Highest probability: ", np.argmax(pdf), "defects with probability of", max(pdf)*100, "%")
    
pieces = 400
defect_rate = .03

HW4_3(pieces, defect_rate)