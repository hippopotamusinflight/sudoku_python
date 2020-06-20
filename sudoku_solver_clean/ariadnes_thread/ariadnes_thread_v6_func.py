#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:11:52 2019 @author: minghan

ARIADNE'S THREAD:
    create ariadnesthread
    take all cells with 2 possibility digits
        test with 1st digit, check if solved
        test with 2nd digit, check if solved
        move on to next cell until solved

"""
#%%
from copy import deepcopy
from ariadnes_solver.partial_solver_v2_func import partial_solver
from check_solved.check_solved_ariadnes_v1 import check_solved_ariadnes
#%%
def ariadnes(puzzle, dictionary):
    puz = deepcopy(puzzle)
    dic = deepcopy(dictionary)
    dic_2s_all = {}
    for d in dic:
        if len(dic[d]) == 2:
            dic_2s_all[d] = dic[d]   
    for d in dic_2s_all:
        for digit in dic_2s_all[d]:
            thread_puz = deepcopy(puz)
            thread_dic = deepcopy(dic)
            thread_puz[d] = digit
            del thread_dic[d]
            thread_puz, thread_dic = partial_solver(thread_puz,thread_dic)
            count_errors = check_solved_ariadnes(thread_puz)
            if count_errors == 0:
                puz = deepcopy(thread_puz)
                break
        else:
            continue
        break
    return(puz)