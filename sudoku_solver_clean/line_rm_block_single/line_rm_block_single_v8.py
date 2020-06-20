'''
LINE REMOVE BLOCK:
    hidden single digit pair in lines,
    use it to eliminate that digit from possibilities in other cells in block
'''
#%%
from collections import Counter
from copy import deepcopy
#%%
def line_rm_block_single(dictionary, rowcol,len_trkr):
    dic = deepcopy(dictionary)
    lanes = [[0,1,2],[3,4,5],[6,7,8]]
    tracker = {}
    for x in range(9):
        line_all_poss = []                                # all possibilities in a line
        for d in dic:
            if d[rowcol] == x:
                line_all_poss.extend(dic[d])
        # return all twin digits in a block
        count2s = Counter(line_all_poss)            # returns dictionary with key=digit, value=count
        pairs_all_digits = [k for k, v in count2s.items() if v == 2]

        same_block_digit = []
        block_id = []
        counter = 0
        for digit in pairs_all_digits:    
            pair_loc = []
            for d in dic:
                if d[rowcol] == x:
                    if digit in dic[d]:
                        pair_loc.append(d)
            if len(pair_loc) == 2:
                # if row/col# of twins in same block
                if (pair_loc[0][1-rowcol] in lanes[0] and pair_loc[1][1-rowcol] in lanes[0]) or \
                    (pair_loc[0][1-rowcol] in lanes[1] and pair_loc[1][1-rowcol] in lanes[1]) or \
                    (pair_loc[0][1-rowcol] in lanes[2] and pair_loc[1][1-rowcol] in lanes[2]):
                    same_block_digit.append(digit)
                    block_id = deepcopy(pair_loc)
#       find block of twins                       
        if len(same_block_digit) == 1:
            for hlane in range(3):             # lane = 0, 1, 2
                for vlane in range(3):
                    if block_id[0][0] in lanes[vlane] and block_id[0][1] in lanes[hlane]:
                        for d in dic:
                            if d[0] in lanes[vlane] and d[1] in lanes[hlane]:
                                if d not in block_id:
                                    if same_block_digit[0] in dic[d]:
                                        if d not in tracker:
                                            tracker[d] = same_block_digit[0]
                                        else:
                                            tracker[d].append(same_block_digit[0])
                                        dic[d].remove(same_block_digit[0])
                                        counter += 1
    print(tracker)
    len_trkr += len(tracker)
    return(dic,len_trkr)