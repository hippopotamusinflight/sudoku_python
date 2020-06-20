#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:31:20 2019

@author: minghan
"""
#%%
from copy import deepcopy
#%%
def check_solved_ariadnes(board):
    solved = deepcopy(board)
    count_error = 0
    for digit in range(1,10):        
        for row in range(9):
            if digit not in solved[row,0:]:
                count_error += 1
        for col in range(9):
            if digit not in solved[0:,col]:
                count_error += 1
        offst = [0,3,6]
        for col in offst:
            for row in offst:           
                if digit not in solved[row:row+3,col:col+3]:
                    count_error += 1
    return(count_error)