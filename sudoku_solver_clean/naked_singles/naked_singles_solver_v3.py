from collections import Counter
from copy import deepcopy
#%% naked_singles: cell has only digit, other cells in region may also have digit
def naked_single_poss(puzzle, dictionary, dictionary_next, len_trkr):
    solving = deepcopy(puzzle)
    dic = deepcopy(dictionary)
    while True:
        counter = 0
        tracker = {}
        singles_list = []
        for k, v in dic.items():
            if len(v) == 1:
                singles_list.append(k)
        if len(singles_list) != 0:
            for s in singles_list:
                solving[s[0],s[1]] = dic[s[0],s[1]][0]
                if s not in tracker:
                    tracker[s] = [dic[s[0],s[1]][0]]
                else:
                    tracker[s].append(dic[s[0],s[1]][0])
                del dic[s[0],s[1]]
                counter += 1
        dic = dictionary_next(solving, dic)
        len_trkr += len(tracker)
        if counter == 0:
            break
    return(solving, dic, len_trkr)