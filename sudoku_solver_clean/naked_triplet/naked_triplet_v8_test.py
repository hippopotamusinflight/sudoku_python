#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Fri Mar 1 17:13:07 2019 @author: minghan

NAKED_TRIPLET:
    some (or all) of the three cells in question may have only 2 out of the 3 candidates
    goal = identify 3 cells with combinations of 3 possibility digits\
        and contain only 2 or 3 of those digits (ie naked)
region_all
triplet_all_combos      combinations of all digits in region
triplet_maybe_digits    using pair combinations for each triplet in triplet_all_combos,
                        count pairs that appear in > 1 cell
                        if exactly 3 pairs appear in > 1 cell, that triplet may be true triplet
triplet_digits          use set()'s .difference() function to find which triplet\
                        has only the triplet digits and NO OTHER DIGITS,
                        if exactly 3 cells gives len(.difference()) result = 0,
triplet_loc             then that triplet and those cells are the true triplets and locations
"""
#%%
from itertools import combinations
from copy import deepcopy
#%%
def naked_triplet_block(dictionary,len_trkr):
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
            # finding true naked_triplet_digits and triplet_locations
            triplet_digits = []
            triplet_loc = []
            for triplet in triplet_maybe_digits:
                count_naked_triplet_cells = 0
                maybe_location = []
                for d in dic:
                    if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                        triplet_set = set(triplet)
                        cell_poss_set = set(dic[d])
                        if len(cell_poss_set.difference(triplet_set)) == 0:
                            count_naked_triplet_cells += 1
                            maybe_location.append(d)
                if count_naked_triplet_cells == 3:
                    triplet_digits = triplet
                    triplet_loc = maybe_location      
            dic_next = deepcopy(dic)
            for d in dic:
                if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                    if d not in triplet_loc:
                        for digit in triplet_digits:
                            if digit in dic[d]:
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
def naked_triplet_rc(dictionary, rowcol,len_trkr):
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
        # finding true naked_triplet_digits and triplet_locations
        triplet_digits = []
        triplet_loc = []
        for triplet in triplet_maybe_digits:
            count_naked_triplet_cells = 0
            maybe_location = []
            for d in dic:
                if d[rowcol] == x:
                    triplet_set = set(triplet)
                    cell_poss_set = set(dic[d])
                    if len(cell_poss_set.difference(triplet_set)) == 0:
                        count_naked_triplet_cells += 1
                        maybe_location.append(d)
            if count_naked_triplet_cells == 3:
                triplet_digits = triplet
                triplet_loc = maybe_location    
        dic_next = deepcopy(dic)
        for d in dic:
            if d[rowcol] == x:
                if d not in triplet_loc:
                    for digit in triplet_digits:
                        if digit in dic[d]:
                            if d not in tracker:
                                tracker[d] = [digit]
                            else:
                                tracker[d].append(digit)
                            dic_next[d].remove(digit)
        dic = deepcopy(dic_next)
    print(tracker)
    len_trkr += len(tracker)    
    return(dic,len_trkr)