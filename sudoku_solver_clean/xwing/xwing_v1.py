#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:03:35 2019

@author: minghan
"""
#%%
from collections import Counter
from itertools import combinations
from copy import deepcopy
#%%
def xwing(dictionary):
    dic = deepcopy(dictionary)
    
#%%
    dic = deepcopy(poss)
    
#%%
    rowcol = 0
    for digit in range(1,10):
#%%
        digit = 3
        wings_loc = []
        for x in range(9):
            count_digit= 0
            locations = []
            for d in dic:
                if d[rowcol] == x:
                    if digit in dic[d]:
                        count_digit += 1
                        locations.append(d)
            if count_digit == 2:
                wings_loc.extend(locations)
#%%
'''damn... (8,7) still has 3'''