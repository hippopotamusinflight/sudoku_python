#%%
from copy import deepcopy
#%%
# sudoku_possibilities_generator
def poss_gen_initial(puzzle):
    solving = deepcopy(puzzle)
    dic = {}
    for x in range(9):          # x = row1,2,3...
        for y in range(9):      # y = col1,2,3...
            if solving[x,y] == 0:
                dic[x,y] = list(range(1,10))    # gives key=coordinate; value=possible digit
    
    # remove based on row, col, quadrant
    for digit in range(1,10):
        for d in dic:
            if digit in solving[d[0],0:]:       # if digit in row, remove from dic at that key
                if digit in dic[d]:
                    dic[d].remove(digit)
            if digit in solving[0:,d[1]]:       # if digit in col, remove from dic at that key
                if digit in dic[d]:
                    dic[d].remove(digit)
            offst = [0,3,6]
            for i in offst:                 # if digit in quadrant, remove from dic at that key
                for j in offst:
                    if i <= d[0] < i+3 and j <= d[1] < j+3:
                        if digit in solving[i:i+3,j:j+3]:
                            if digit in dic[d]:
                                dic[d].remove(digit)
    return(dic)
#%%
def poss_gen_next(puzzle, dictionary):
    solving = deepcopy(puzzle)
    dic_init = deepcopy(dictionary)
    tracker = {}
    for digit in range(1,10):
        for d in dic_init:
            if digit in solving[d[0],0:]:       # if digit in row, remove from dic_init at that key
                if digit in dic_init[d]:
                    if d not in tracker:
                        tracker[d] = [digit]
                    else:
                        tracker[d].append(digit)
                    dic_init[d].remove(digit)

            if digit in solving[0:,d[1]]:       # if digit in col, remove from dic_init at that key
                if digit in dic_init[d]:
                    if d not in tracker:
                        tracker[d] = [digit]
                    else:
                        tracker[d].append(digit)
                    dic_init[d].remove(digit)

            offst = [0,3,6]
            for i in offst:                 # if digit in quadrant, remove from dic_init at that key
                for j in offst:
                    if i <= d[0] < i+3 and j <= d[1] < j+3:
                        if digit in solving[i:i+3,j:j+3]:
                            if digit in dic_init[d]:
                                if d not in tracker:
                                    tracker[d] = [digit]
                                else:
                                    tracker[d].append(digit)
                                dic_init[d].remove(digit)

    dic_next = deepcopy(dic_init)
    for i in range(9):
        for j in range(9):
            if solving[i,j] != 0 and (i,j) in dic_init:
                del dic_next[(i,j)]
                if d not in tracker:
                    tracker[(i,j)] = [solving[i,j]]
                else:
                    tracker[(i,j)].append(solving[i,j])
    print(tracker)
    return(dic_next)








