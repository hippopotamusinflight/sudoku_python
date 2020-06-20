# sudoku solver (time = 2-10seconds)

#%% IMPORTS
import numpy as np
import random
from timeit import default_timer as timer

#%%
def shuffl(nd):
    nums = [x for x in range(nd)]
    random.shuffle(nums)
    return(nums)

#%%
start = timer()

board = []                              # initialize board
for _ in range(9):
    board.append([0]*9)
board = np.array(board)

while 0 in board.flatten():
    board = []
    for _ in range(9):
        board.append([0]*9)
    board = np.array(board)

    offst = [0,3,6]                             # with i,j loops, goes through 9 quadrants
    for i in offst:                                  # i = 0, 3, 6
        for j in offst:                              # j = 0, 3, 6
            for k in range(10):                 # cycles through numbers 1 to 9
                q = board[j:j+3,i:i+3]
                locale = np.where(q == 0)       # finding locations of zeros
                ordr = shuffl(len(locale[0]))   # use shuffl fn to randomly assign number to location
                for l in ordr:
                    if k in q:                                  # if k not in quadrant -> break out of for loop
                        break
                    elif k not in board[locale[0][l]+j,0:]:     # if k not in column 
                        if k not in board[0:,locale[1][l]+i]:   # if k not in row
                            board[locale[0][l]+j,locale[1][l]+i] = k
print(board)

end = timer()
print(end - start)
