#-*- coding: utf-8 -*-
"""
http://elementsofprogramminginterviews.com/sample/epilight_python_new.pdf
"""
import copy
def comb_set_recursively(S, i, chosen=[]):
    ans = []
    #print("debugging: %s, %s" % (i, chosen))
    if i == len(S):
        #print(chosen)
        return chosen
    else:
        not_chosen = copy.copy(chosen)
        its_chosen = copy.copy(chosen)
        its_chosen.append(S[i])
        i+=1
        ans.append(comb_set_recursively(S, i, not_chosen))
        ans.append(comb_set_recursively(S, i, its_chosen))
        return ans

def comb_set(S):
    return comb_set_recursively(S, 0, [])
    #return comb_set_iteratively(S)

def comb_set_iteratively(S):
    ans = []
    for bits in range(2**len(S)):
        bits_str = "{0:b}".format(bits).zfill(len(S))
        #print(bits_str)
        tmp = []
        for i, b in enumerate(bits_str):
            if int(b) == 1:
                tmp.append(S[i])
        #print(tmp)
        ans.append(tmp)
    for a in ans: print(a)

print(comb_set([1, 2, 3]))
#print(comb_set([1, 2, 4, 5, 6]))
