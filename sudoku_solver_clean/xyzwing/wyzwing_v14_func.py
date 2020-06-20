#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:27:07 2019 @author: minghan

XYZ WING:
    x&y in same block
        z cell in different block, but same row as x
        y cell cannot be same row as x&z (or else becomes naked triplet)
    x = pivot, y and z are pinchers
        x has all 3 candidates; y share 2 digits with x;
        z has 1 digit not shared btw x&y, and 1 digit shared btw x&y (2 possibilities)
    in x&y block:
        cells (max 2) in row of x, 
        if has possibility digit shared btw x&y&z, 
            digit removed
"""
#%%
from itertools import combinations
from copy import deepcopy
#%%
def xyzwing(dictionary, rowcol,len_trkr):
    dic = deepcopy(dictionary)
    dic_next = deepcopy(dic)
    lanes = [[0,1,2],[3,4,5],[6,7,8]]
    tracker = {}
    dic_2s_all = {}
    dic_2or3_all = {}
    for d in dic:
        if len(dic[d]) == 2:
            dic_2s_all[d] = dic[d]
        if 1 < len(dic[d]) < 4:
            dic_2or3_all[d] = dic[d]
    for col in [0,3,6]:
        for row in [0,3,6]:
            dic_2or3_block = {}
            for d in dic_2or3_all:
                if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                    dic_2or3_block[d] = dic_2or3_all[d]
            dic_2or3_block_list = []
            for d in dic_2or3_block:
                dic_2or3_block_list.append(dic_2or3_block[d])
            dic_2or3_block_combos = []
            for combos in combinations(dic_2or3_block_list, 2):
                dic_2or3_block_combos.append(combos)
            maybe_xyz = []
            for combos in dic_2or3_block_combos:
                x_set = set()
                y_set = set()
                # either length is 2,3 or 3,2
                if len(combos[0]) == 3:
                    x_set = set(combos[0])
                    if len(combos[1]) == 2:
                        y_set = set(combos[1])
                if len(combos[0]) == 2:
                    y_set = set(combos[0])
                    if len(combos[1]) == 3:
                        x_set = set(combos[1])
                if len(x_set) == 3 and len(y_set) == 2:
                    if len(x_set.intersection(y_set)) == 2:
                        # z 1st digit = could be either digit shared by x and y
                        z_1st_digits = list(x_set.intersection(y_set))
                        # z 2nd digit = has to be digit in x but NOT in y
                        z_2nd_digit = list(x_set.difference(y_set))
                        maybe_xyz.append([x_set,y_set,z_1st_digits,z_2nd_digit])
                # [[{2, 4, 8}, {2, 8}, [8, 2], [4]]]
            for xyz in maybe_xyz:
                x_pos = list(dic_2or3_block.keys())\
                [list(dic_2or3_block.values()).index(sorted(list(xyz[0])))]
                # x_pos = (0,6), a tuple
                x_digits = set()
                y_digits = set()
                y_pos = ()
                z_digits = set()
                for d in dic_2s_all:
                    if d[rowcol] == x_pos[rowcol]:
                        # x and z cannot be same row
                        if (d[1-rowcol] in lanes[0] and x_pos[1-rowcol] not in lanes[0]) or\
                        (d[1-rowcol] in lanes[1] and x_pos[1-rowcol] not in lanes[1]) or\
                        (d[1-rowcol] in lanes[2] and x_pos[1-rowcol] not in lanes[2]):
                            for digit in xyz[2]:
                                # xyz[3][0] = z 2nd digit
                                if len(set([digit,xyz[3][0]]).difference(set(dic_2s_all[d]))) == 0:
                                    x_digits = xyz[0]
                                    y_digits = xyz[1]
                                    y_pos = list(dic_2or3_block.keys())\
                                    [list(dic_2or3_block.values()).index(sorted(list(xyz[1])))]
                                    z_digits = set([digit,xyz[3][0]])
                shared_digit = list(x_digits.intersection(y_digits,z_digits))
                if len(shared_digit) == 1:
                    for d in dic:
                        if d != x_pos:
                            if d[0] == x_pos[0]:
                                if x_pos[0] != y_pos[0]:
                                    if (d[1] in lanes[0] and x_pos[1] in lanes[0]) or\
                                    (d[1] in lanes[1] and x_pos[1] in lanes[1]) or\
                                    (d[1] in lanes[2] and x_pos[1] in lanes[2]):
                                        if shared_digit[0] in dic_next[d]:
                                            tracker[d] = shared_digit[0]
                                            dic_next[d].remove(shared_digit[0])
    print(tracker)
    len_trkr += len(tracker)
    return(dic_next,len_trkr)