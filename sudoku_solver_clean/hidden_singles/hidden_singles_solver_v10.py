from collections import Counter
from copy import deepcopy
#%% hidden_singles: cell may have other poss, but digit unique in region 
def hidden_single_poss(puzzle, dictionary, dictionary_next, len_trkr):
    solving = deepcopy(puzzle)
    dic = deepcopy(dictionary)
    dic_updated = deepcopy(dictionary)
    # find singles in block and update board    
    tracker = {}
    offst = [0,3,6]                             # with i,j loops, goes through 9 quadrants
    for i in offst:                                  # i = col 0, 3, 6
        for j in offst:                              # j = row 0, 3, 6
            block_all = []
            for d in dic:
                if d[0] in range(j,j+3) and d[1] in range(i,i+3):           
                    block_all.extend(dic[d])
            count1s = Counter(block_all)            # returns dictionary with key=digit, value=count
            single = [k for k, v in count1s.items() if v == 1]       # returns digits with count == 2

            if len(single) == 1:
                for d in dic:
                    if d[0] in range(j,j+3) and d[1] in range(i,i+3):
                        if single[0] in dic[d]:
                            solving[d[0],d[1]] = single[0]
                            if d not in tracker:
                                tracker[d] = [single[0]]
                            else:
                                tracker[d].append(single[0])
                            del dic_updated[d]
    dic_updated = dictionary_next(solving, dic_updated)

    # find singles in row and update board    
    dic_updated2 = deepcopy(dic_updated)
    for r in range(9):
        row_all = []
        for d in dic_updated:
            if d[0] == r:       # rows 0 to 8
                row_all.extend(dic_updated[d])
        count1s = Counter(row_all)
        single = [k for k, v in count1s.items() if v == 1]       # returns digits with count == 2
        if len(single) == 1:
            for d in dic_updated:
                if d[0] == r:
                    if single[0] in dic_updated[d]:
                        solving[d[0],d[1]] = single[0]
                        if d not in tracker:
                            tracker[d] = [single[0]]
                        else:
                            tracker[d].append(single[0])
                        del dic_updated2[d]
    dic_updated2 = dictionary_next(solving, dic_updated2)

    # find singles in col and update board    
    dic_updated3 = deepcopy(dic_updated2)
    for c in range(9):
        col_all = []
        for d in dic_updated2:
            if d[1] == c:       # rows 0 to 8
                col_all.extend(dic_updated2[d])
        count1s = Counter(col_all)
        single = [k for k, v in count1s.items() if v == 1]       # returns digits with count == 2
        if len(single) == 1:
            for d in dic_updated2:
                if d[1] == c:
                    if single[0] in dic_updated2[d]:
                        solving[d[0],d[1]] = single[0]
                        if d not in tracker:
                            tracker[d] = [single[0]]
                        else:
                            tracker[d].append(single[0])
                        del dic_updated3[d]
    dic_updated3 = dictionary_next(solving, dic_updated3)
    len_trkr += len(tracker)
    print(tracker)
    return(solving, dic_updated3, len_trkr)