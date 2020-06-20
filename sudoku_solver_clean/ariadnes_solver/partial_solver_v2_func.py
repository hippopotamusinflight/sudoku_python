#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 07:39:51 2019 @author: minghan

PARTIAL SOLVER
    taken from solver
    but inputs both puzzle and dictionary
    returns both puzzle and dictionary
"""
#%%
import sys
sys.path.append('/Users/minghan/Google Drive/ProgrammingCodeBioinformatics/2019_sudoku_python/sudoku_solvers')
#%%
from copy import deepcopy
from poss_gen.poss_gen_v7 import poss_gen_next

from naked_singles.naked_singles_solver_v3 import naked_single_poss
from naked_pairs.naked_pairs_v4_cleaned_up import naked_pairs_rc, naked_pairs_blocks
from naked_triplet.naked_triplet_v8_test import naked_triplet_rc, naked_triplet_block

from hidden_pairs.hidden_pairs_v7_with_docstring import hidden_pairs_blocks, hidden_pairs_rc
from hidden_singles.hidden_singles_solver_v10 import hidden_single_poss
from hidden_triplet.hidden_triplet_v5 import hidden_triplet_rc, hidden_triplet_block

from line_rm_block_single.line_rm_block_single_v8 import line_rm_block_single
from block_rm_line_single.block_rm_line_single_v1 import block_rm_line_single
from xyzwing.wyzwing_v14_func import xyzwing

#%%
def partial_solver(puzzle, dictionary):
    board = deepcopy(puzzle)
    poss = deepcopy(dictionary)
    while True:
        len_trkr = 0
        board, poss, len_trkr = naked_single_poss(board, poss, poss_gen_next, len_trkr)
        poss,len_trkr = naked_pairs_rc(poss,0,len_trkr)
        poss,len_trkr = naked_pairs_rc(poss,1,len_trkr)        
        poss,len_trkr = naked_pairs_blocks(poss,len_trkr)
        poss,len_trkr = naked_triplet_rc(poss,0,len_trkr)
        poss,len_trkr = naked_triplet_rc(poss,1,len_trkr)
        poss,len_trkr = naked_triplet_block(poss,len_trkr)
        board, poss, len_trkr = hidden_single_poss(board, poss, poss_gen_next, len_trkr)
        poss,len_trkr = hidden_pairs_rc(poss,0,len_trkr)
        poss,len_trkr = hidden_pairs_rc(poss,1,len_trkr)
        poss,len_trkr = hidden_pairs_blocks(poss,len_trkr)
        poss,len_trkr = hidden_triplet_rc(poss,0,len_trkr)
        poss,len_trkr = hidden_triplet_rc(poss,1,len_trkr)
        poss,len_trkr = hidden_triplet_block(poss,len_trkr)
        poss,len_trkr = line_rm_block_single(poss,0,len_trkr)
        poss,len_trkr = line_rm_block_single(poss,1,len_trkr)        
        poss,len_trkr = block_rm_line_single(poss,len_trkr)
        poss,len_trkr = xyzwing(poss,0,len_trkr)
        poss,len_trkr = xyzwing(poss,1,len_trkr)
        if len_trkr == 0:
            break
    return(board, poss)