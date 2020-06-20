# sudoku_combined_solver
#%%
import sys
sys.path.append('/Users/minghan/Google Drive/ProgrammingCodeBioinformatics/2019_sudoku_python/sudoku_solvers')
#%%
import numpy as np
from copy import deepcopy
from poss_gen.poss_gen_v7 import poss_gen_initial
from ariadnes_thread.ariadnes_thread_v6_func import ariadnes
from ariadnes_solver.partial_solver_v2_func import partial_solver
from check_solved.check_solved_ariadnes_v1 import check_solved_ariadnes
#%%
def solver(puzzle):
    board = deepcopy(puzzle)
    poss = poss_gen_initial(board)
    board, poss = partial_solver(board,poss)
    count_errors = check_solved_ariadnes(board)
    if count_errors == 0:
        return(board)
    else:
        board = ariadnes(board, poss)
        return(board)
