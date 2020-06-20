#%%
from copy import deepcopy
#%%
'''
no need to invert dictionary...
instead use below
list(mydict.keys())[list(mydict.values()).index(16)]
'''
#%% sudoku_possibilities_solve_v1
def naked_pairs_rc(dictionary, rowcol, len_trkr):
    dic = deepcopy(dictionary)
    tracker = {}
    for x in range(9):
        dic_list = {}
        dic_tup = {}
        for d in dic:                   # goes through keys in dic
            if d[rowcol] == x:
        # convert values to tuples before inverting dic_col
                dic_tup[d] = tuple(dic[d])     # sub-dictionary of dic with col = 4
                twos = []
        # inverting dic_col
                inv_dic = {}
                for key, value in dic_tup.items():    
                    if value not in inv_dic:
                        inv_dic[value] = [key]
                    else:
                        inv_dic[value].append(key)
                for key,value in inv_dic.items():
                    if len(key) == 2 and len(value) == 2:
                        twos = key
                it = [key for key, value in dic_tup.items() if value == twos]
        # change values for dic_col back into list
                dic_list[d] = dic[d]
        
                dic_other = {}
                for d in dic_list:
                    if d not in it:
                        dic_other[d] = dic_list[d]
        
                for a in twos:
                    for other in dic_other:
                        if a in dic_other[other]:
                            if other not in tracker:
                                tracker[other] = [a]
                            else:
                                tracker[other].append(a)
                            dic[other].remove(a)
    print(tracker)
    len_trkr += len(tracker)                        
    return(dic, len_trkr)
#%%
def naked_pairs_blocks(dictionary, len_trkr):
    dic = deepcopy(dictionary)
    tracker = {}
    offst = [0,3,6]                             # with i,j loops, goes through 9 quadrants
    for i in offst:                                  # i = col 0, 3, 6
        for j in offst:
            dic_list = {}
            dic_tup = {}
            for d in dic:                   # goes through keys in dic
                if d[0] in range(j,j+3) and d[1] in range(i,i+3):
            # convert values to tuples before inverting dic_col
                    dic_tup[d] = tuple(dic[d])     # sub-dictionary of dic with col = 4
                    twos = []
            # inverting dic_col
                    inv_dic = {}
                    for key, value in dic_tup.items():    
                        if value not in inv_dic:
                            inv_dic[value] = [key]
                        else:
                            inv_dic[value].append(key)
                    for key,value in inv_dic.items():
                        if len(key) == 2 and len(value) == 2:
                            twos = key
                    it = [key for key, value in dic_tup.items() if value == twos]
            # change values for dic_col back into list
                    dic_list[d] = dic[d]            
                    dic_other = {}
                    for d in dic_list:
                        if d not in it:
                            dic_other[d] = dic_list[d]            
                    for a in twos:
                        for other in dic_other:
                            if a in dic_other[other]:
                                if other not in tracker:
                                    tracker[other] = [a]
                                else:
                                    tracker[other].append(a)
                                dic[other].remove(a)
    print(tracker)
    len_trkr += len(tracker)    
    return(dic, len_trkr)