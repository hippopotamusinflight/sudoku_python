#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:25:06 2019

@author: minghan
"""
#%%
from collections import Counter
from itertools import combinations
from copy import deepcopy
#%%
def hidden_triplet_block(dictionary,len_trkr):
    dic = deepcopy(dictionary)
    tracker = {}
    for col in [0,3,6]:
        for row in [0,3,6]:
            region_all = set()
            for d in dic:
                if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                    for digit in dic[d]:
                        region_all.add(digit)
            triplet_all_combos = []
            for p in combinations(region_all, 3):
                triplet_all_combos.append(list(p))
            triplet_maybe_digits = []
            for triplet in triplet_all_combos:
                count_3_pairs = 0
                for pair in combinations(triplet,2):
                    count_cells = 0            
                    for d in dic:
                        if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                            if pair[0] in dic[d] and pair[1] in dic[d]:
                                count_cells += 1
                    if count_cells > 0:
                        count_3_pairs += 1
                if count_3_pairs == 3:
                    triplet_maybe_digits.append(triplet)
    
            # finding true hidden_triplet_digits and triplet_locations
            triplet_digits = []
            triplet_loc = []
            for triplet in triplet_maybe_digits:
                count_hidden_triplet_cells = 0
                maybe_location = []
                for d in dic:
                    if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                        triplet_set = set(triplet)
                        cell_poss_set = set(dic[d])
                        if len(cell_poss_set.intersection(triplet_set)) > 0:
                            count_hidden_triplet_cells += 1
                            maybe_location.append(d)
                if count_hidden_triplet_cells == 3:
                    triplet_digits = triplet
                    triplet_loc = maybe_location
            dic_next = deepcopy(dic)
            for d in dic:
                if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                    if d in triplet_loc:
                        for digit in dic[d]:
                            if digit not in triplet_digits:
                                if d not in tracker:
                                    tracker[d] = [digit]
                                else:
                                    tracker[d].append(digit)
                                dic_next[d].remove(digit)
            dic = deepcopy(dic_next)
    print(tracker)
    len_trkr += len(tracker)
    return(dic,len_trkr)
#%%
def hidden_triplet_rc(dictionary, rowcol,len_trkr):
    dic = deepcopy(dictionary)
    tracker = {}
    for x in range(9):
        region_all = set()
        for d in dic:
            if d[rowcol] == x:
                for digit in dic[d]:
                    region_all.add(digit)
        triplet_all_combos = []
        for p in combinations(region_all, 3):
            triplet_all_combos.append(list(p))
        triplet_maybe_digits = []
        for triplet in triplet_all_combos:
            count_3_pairs = 0
            for pair in combinations(triplet,2):
                count_cells = 0            
                for d in dic:
                    if d[rowcol] == x:
                        if pair[0] in dic[d] and pair[1] in dic[d]:
                            count_cells += 1
                if count_cells > 0:
                    count_3_pairs += 1
            if count_3_pairs == 3:
                triplet_maybe_digits.append(triplet)

        # finding true hidden_triplet_digits and triplet_locations
        triplet_digits = []
        triplet_loc = []
        for triplet in triplet_maybe_digits:
            count_hidden_triplet_cells = 0
            maybe_location = []
            for d in dic:
                if d[rowcol] == x:
                    triplet_set = set(triplet)
                    cell_poss_set = set(dic[d])
                    if len(cell_poss_set.intersection(triplet_set)) > 0:
                        count_hidden_triplet_cells += 1
                        maybe_location.append(d)
            if count_hidden_triplet_cells == 3:
                triplet_digits = triplet
                triplet_loc = maybe_location
        dic_next = deepcopy(dic)
        for d in dic:
            if d[rowcol] == x:
                if d in triplet_loc:
                    for digit in dic[d]:
                        if digit not in triplet_digits:
                            if d not in tracker:
                                tracker[d] = [digit]
                            else:
                                tracker[d].append(digit)
                            dic_next[d].remove(digit)
        dic = deepcopy(dic_next)
    print(tracker)
    len_trkr += len(tracker)
    return(dic,len_trkr)