# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:37:08 2018

@author: NAO
"""

import numpy as np
from numpy.linalg import inv

def HW2_Q2():
    
    trans_matrix = np.matrix([[ 1,  0,  0,  0,  0,  0],
                              [ 0,  1,  0,  0,  0,  0],
                              [ 0,  0,  1,  0,  0,  0],
                              [.1, .2, .3,  0, .1, .3],
                              [.2, .4,  0, .2, .2,  0],
                              [.1,  0,  0, .3, .3, .3]])
    
    i_matrix = np.matrix([[trans_matrix[0,0], trans_matrix[0,1], trans_matrix[0,2]],
                          [trans_matrix[1,0], trans_matrix[1,1], trans_matrix[1,2]],
                          [trans_matrix[2,0], trans_matrix[2,1], trans_matrix[2,2]]])
    
    q_matrix = np.matrix([[trans_matrix[3,3], trans_matrix[3,4], trans_matrix[3,5]],
                          [trans_matrix[4,3], trans_matrix[4,4], trans_matrix[4,5]],
                          [trans_matrix[5,3], trans_matrix[5,4], trans_matrix[5,5]]])
    
    r_matrix = np.matrix([[trans_matrix[3,0], trans_matrix[3,1], trans_matrix[3,2]],
                          [trans_matrix[4,0], trans_matrix[4,1], trans_matrix[4,2]],
                          [trans_matrix[5,0], trans_matrix[5,1], trans_matrix[5,2]]])
    
    f_matrix = (i_matrix - q_matrix)
    
    f_matrix = inv(f_matrix)
    
    fr_matrix = f_matrix * r_matrix
    
    lim_trans_matrix = np.matrix([[trans_matrix[0,0], trans_matrix[0,1], trans_matrix[0,2], trans_matrix[0,3], trans_matrix[0,4], trans_matrix[0,5]],
                                  [trans_matrix[1,0], trans_matrix[1,1], trans_matrix[1,2], trans_matrix[1,3], trans_matrix[1,4], trans_matrix[1,5]],
                                  [trans_matrix[2,0], trans_matrix[2,1], trans_matrix[2,2], trans_matrix[2,3], trans_matrix[2,4], trans_matrix[2,5]],
                                  [fr_matrix[0,0], fr_matrix[0,1], fr_matrix[0,2], 0, 0, 0],
                                  [fr_matrix[1,0], fr_matrix[1,1], fr_matrix[1,2], 0, 0, 0],
                                  [fr_matrix[2,0], fr_matrix[2,1], fr_matrix[2,2], 0, 0, 0]])
    
    print(lim_trans_matrix)
    
HW2_Q2()