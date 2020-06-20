'''
HIDDEN_PAIR: 
    if in a region 2 possibility digits are only found in 2 cells,
    then all other possibilities can be eliminated from those 2 cells
region_all_poss         all possibilities in block/row/col
count2s                 dictionary with key=digit, value=count
pairs_all_digits        digits with count==2
pairs_all_combos        list of all possible combination of digits with count==2
narrowed_down_loc       location of all possible combination of digits with count==2
narrowed_down_all_poss  all possibility digits in paired_list_loc
countpairs              in 
                    
'''
#%%
from collections import Counter
from itertools import combinations
from copy import deepcopy
#%% update possibilities dictionary based on hidden_pairs
def hidden_pairs_blocks(dictionary,len_trkr):
    dic = deepcopy(dictionary)
    tracker = {}
    for col in [0,3,6]:
        for row in [0,3,6]:
            region_all_poss = []
            for d in dic:
                if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                    region_all_poss.extend(dic[d])
            count2s = Counter(region_all_poss)
            pairs_all_digits = [k for k, v in count2s.items() if v == 2]
            pairs_all_combos = []
            for p in combinations(pairs_all_digits, 2):
                pairs_all_combos.append(list(p))
            narrowed_down_loc = set()
            for d in dic:
                if d[0] in range(row,row+3) and d[1] in range(col,col+3):
                    for p in pairs_all_combos:
                        if p[0] in dic[d] and p[1] in dic[d]:
                            narrowed_down_loc.add(d)
            narrowed_down_all_poss = []
            for loc in narrowed_down_loc:
                for d in dic:
                    if d == loc:
                        narrowed_down_all_poss.extend(dic[d])
            countpairs = Counter(narrowed_down_all_poss)
            # find hidden pairs
            hidden_pair = []
            for digit in countpairs:             # narrowed_down_loc now have false pairs
                if digit in pairs_all_digits:    # only when digit also found in original pairs list
                    if countpairs[digit] == 2:
                        hidden_pair.extend([digit])
            # remove all other possibilities from pair cells
            if len(hidden_pair) == 2:
                for loc in narrowed_down_loc:
                    for d in dic:                   # use filter() ???
                        if d == loc:
                            if hidden_pair[0] in dic[d] and hidden_pair[1] in dic[d]:
                                if dic[d] != hidden_pair:
                                    if d not in tracker:
                                        tracker[d] = hidden_pair
                                    else:
                                        tracker[d].append(hidden_pair)
                                dic[d] = deepcopy(hidden_pair)
                                # must be something about this assignment
    print(tracker)
    len_trkr += len(tracker)
    return(dic,len_trkr)
#%%
def hidden_pairs_rc(dictionary, rowcol,len_trkr):
    dic = deepcopy(dictionary)
    tracker = {}
    for x in range(9):
        region_all_poss = []
        for d in dic:
            if d[rowcol] == x:
                region_all_poss.extend(dic[d])
        # return all twin digits in a block
        count2s = Counter(region_all_poss)            # returns dictionary with key=digit, value=count
        pairs_all_digits = [k for k, v in count2s.items() if v == 2]       # returns digits with count == 2
        # pairs_all_combos = list of list of combinations of twin digits in a block
        pairs_all_combos = []
        for p in combinations(pairs_all_digits, 2):
            pairs_all_combos.append(list(p))
        narrowed_down_loc = []
        for d in dic:
            if d[rowcol] == x:
                for p in pairs_all_combos:
                    if p[0] in dic[d] and p[1] in dic[d]:
                        if d not in narrowed_down_loc:
                            narrowed_down_loc.append(d)
        narrowed_down_all_poss = []
        for loc in narrowed_down_loc:
            for d in dic:
                if d == loc:
                    narrowed_down_all_poss.extend(dic[d])
        countpairs = Counter(narrowed_down_all_poss)
        # find hidden pairs
        hidden_pair = []
        for digit in countpairs:  
            if digit in pairs_all_digits:
                if countpairs[digit] == 2:
                    hidden_pair.extend([digit])
        # remove all other possibilities from pair cells
        if len(hidden_pair) == 2:
            for loc in narrowed_down_loc:
                for d in dic:
                    if d == loc:
                        if hidden_pair[0] in dic[d] and hidden_pair[1] in dic[d]:
                            if dic[d] != hidden_pair:
                                if d not in tracker:
                                    tracker[d] = hidden_pair
                                else:
                                    tracker[d].append(hidden_pair)
                            dic[d] = deepcopy(hidden_pair)
    print(tracker)
    len_trkr += len(tracker)    
    return(dic,len_trkr)