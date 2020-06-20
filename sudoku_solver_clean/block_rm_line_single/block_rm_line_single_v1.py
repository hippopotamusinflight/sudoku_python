#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:50:40 2019

@author: minghan
"""
#%%
from collections import Counter
from copy import deepcopy
#%%
def block_rm_line_single(dictionary,len_trkr):
    dic = deepcopy(dictionary)
    tracker = {}
    for col in [0,3,6]:
        for row in [0,3,6]:
            region_all_poss = []
            for d in dic:
                if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                    region_all_poss.extend(dic[d])
            count2s = Counter(region_all_poss)
            pairs_all_digits = [k for k, v in count2s.items() if v == 2]

            for digit in pairs_all_digits:
                pair_loc = []
                for d in dic:
                    if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                        if digit in dic[d]:
                            pair_loc.append(d)

                if pair_loc[0][0] == pair_loc[1][0]:
                    for d in dic:
                        if d[0] == pair_loc[0][0] and d not in pair_loc:
                            if digit in dic[d]:
                                if d not in tracker:
                                    tracker[d] = [digit]
                                else:
                                    tracker[d].append(digit)
                                dic[d].remove(digit)
                if pair_loc[0][1] == pair_loc[1][1]:
                    for d in dic:
                        if d[1] == pair_loc[0][1] and d not in pair_loc:
                            if digit in dic[d]:
                                if d not in tracker:
                                    tracker[d] = [digit]
                                else:
                                    tracker[d].append(digit)                                
                                dic[d].remove(digit)     
    print(tracker)
    len_trkr += len(tracker)
    return(dic,len_trkr)