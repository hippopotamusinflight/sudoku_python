'''
SUDOKU PUZZLE SOLVER
    input puzzle name
    
'''
#%%
import sys
sys.path.append('/Users/minghan/Google Drive/ProgrammingCodeBioinformatics/2019_sudoku_python/sudoku_solvers')
from combined_solver.combined_solver_v31_clean import solver
#%%
sudoku_puzzle = input("enter puzzle name: ")
board = solver(sudoku_puzzle); print(board)
#%%
board = solver(puzzle2); print(board)