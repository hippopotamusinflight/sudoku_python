#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:31:20 2019

@author: minghan
"""
#%%
from copy import deepcopy
#%%
def check_solved(board):
    solved = deepcopy(board)
    wrongs_row = 0
    wrongs_col = 0
    wrongs_block = 0
    error_row = []
    error_col = []
    error_block = []
    for digit in range(1,10):        
        for row in range(9):
            if digit not in solved[row,0:]:
                error_row.append(row + 1)
                wrongs_row += 1
        for col in range(9):
            if digit not in solved[0:,col]:
                error_col.append(col + 1)
                wrongs_col += 1
        offst = [0,3,6]
        for col in offst:
            for row in offst:
                if col == 0 and row == 0: block = 1
                if col == 3 and row == 0: block = 2
                if col == 6 and row == 0: block = 3
                if col == 0 and row == 3: block = 4
                if col == 3 and row == 3: block = 5
                if col == 6 and row == 3: block = 6
                if col == 0 and row == 6: block = 7
                if col == 3 and row == 6: block = 8
                if col == 6 and row == 6: block = 9                
                if digit not in solved[row:row+3,col:col+3]:
                    error_block.append(block)
                    wrongs_block += 1
    if wrongs_row == 0 and wrongs_col == 0:
        print("SOLVED")
    if wrongs_row != 0:
        print("ERROR in " + str(wrongs_row) + " cell(s), row(s): " + str(error_row))
    if wrongs_col != 0:
        print("ERROR in " + str(wrongs_col) + " cell(s), col(s): " + str(error_col))
    if wrongs_block != 0:
        print("ERROR in " + str(wrongs_block) + " cell(s), block(s): " + str(error_block))
