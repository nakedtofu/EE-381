# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 07:46:21 2018

@author: NAO
"""

import numpy as np
from numpy.linalg import inv

def HW2_Q1():
    
    i = 0
    
    flag = 0
                              #d,  c,  b,   a
    trans_matrix = np.matrix([[  1,  0,   0,  0], #d
                              [  0,  1,   0,  0], #c
                              [.45,  0, .35, .2], #b
                              [ .3, .3,  .1, .3]]) #a
    
    i_matrix = np.matrix([[trans_matrix[0,0], trans_matrix[0,1]],
                          [trans_matrix[1,0], trans_matrix[1,1]]])
    
    q_matrix = np.matrix([[trans_matrix[2,2], trans_matrix[2,3]],
                          [trans_matrix[3,2], trans_matrix[3,3]]])
    
    r_matrix = np.matrix([[trans_matrix[2,0], trans_matrix[2,0]],
                          [trans_matrix[3,1], trans_matrix[3,1]]])
    
    f_matrix = (i_matrix - q_matrix)
    
    f_matrix = inv(f_matrix)
    
    fr_matrix = f_matrix * r_matrix
    
    lim_trans_matrix = np.matrix([[trans_matrix[0,0], trans_matrix[0,1], trans_matrix[0,2], trans_matrix[0,3]],
                                  [trans_matrix[1,0], trans_matrix[1,1], trans_matrix[1,2], trans_matrix[1,3]],
                                  [fr_matrix[0,0], fr_matrix[0,1], 0, 0],
                                  [fr_matrix[1,0], fr_matrix[1,1], 0, 0]])
                                 
    print(trans_matrix)
    
    print(lim_trans_matrix)
    
    stable_lim_trans_matrix = np.matrix([[.25,   0,  0,  0],
                                         [  0, .15,  0,  0],
                                         [  0,   0, .3,  0],
                                         [  0,   0,  0, .3]]) * lim_trans_matrix
    
    stable_matrix = np.matrix([[.25,   0,  0,  0],
                               [  0, .15,  0,  0],
                               [  0,   0, .3,  0],
                               [  0,   0,  0, .3]]) * trans_matrix
    
    print(stable_lim_trans_matrix)
    
    while flag == 0:
        if((round(stable_matrix[2, 0], 2) == round(stable_lim_trans_matrix[2, 0], 2))):
            flag = 1
        else:
           stable_matrix = stable_matrix * trans_matrix
           i = i + 1
        
    print(stable_matrix, "at", i, "th iteration.")
    
HW2_Q1()
