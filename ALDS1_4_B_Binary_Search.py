#-*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B
"""
import itertools
def input_array():
    n = int(input())
    S = list(map(int, input().split()))
    return S

def input_from_txt(number=1):
    import requests
    #url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_4_A/8/in"
    url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_4_B/%s/in" % number
    res = requests.get(url)
    input = res.text.split("\n")
    n = input[0]
    S = list(map(int, input[1].split()))
    q = input[2]
    T = list(map(int, input[3].split()))
    return (n, S, q, T)

# O(n^2)
def get_set(S, T):
    C = []
    for s in S:
        for t in T:
            if s == t: C.append(t)
    return C

# O(n^2) ??
def get_set2(S, T):
    return list(set(S).intersection(set(T)))

# O(log(n)) + O(n+q) = O(n)
def get_set3(S:list, T:list):
    D:dict = {}
    C = []
    for s in S:
        D[s] = 1
    for t in T:
        if t in D.keys() and D[t] == 1:
            D[t] = 2
            C.append(t)
    return C

def pick_base(array_sz):
    base_idx = int((array_sz-1)/2)  # O(n)
    return base_idx

def debug(*args):
    #print(args)
    pass

def binary_search_SLOW(x:int, lst:list):
    debug("= start =%s" % ("="*20))
    while len(lst) > 0: # O(1)
        base_idx = pick_base(len(lst))
        t = lst[base_idx]
        #debug("%s" % lst)
        #debug("%s" % list(range(len(lst))))
        debug("base_idx %s cur %s and looking for %s" % (base_idx, t, x))
        if t == x:
            debug("found!!!!!")
            return True
        elif len(lst) == 1: return False
        elif x < t:
            #lst = lst[:base_idx]
            lst = list(itertools.islice(lst, 0, base_idx))
            debug("keep left: %s" % lst)
        else:
            #lst = lst[base_idx+1:]
            lst = list(itertools.islice(lst, base_idx+1, len(lst)))
            debug("keep right: %s" % lst)
    return False





def binary_search_verbose(x:int, lst:list):
    #debug("= start =%s" % ("="*20))
    si = 0 # start index
    ei = len(lst)-1 # end index
    #print("########", end="", flush=True)
    while ei - si > 0: # O(1)
        base_idx = si+pick_base(ei - si)
        #base_idx = int((ei - si) / 2)
        t = lst[base_idx]
        #print(".", end="", flush=True)
        #debug("%s" % lst)
        #debug("%s" % list(range(len(lst))))
        #debug("base_idx %s cur %s and looking for %s" % (base_idx, t, x))
        if t == x:
            #debug("found!!!!!")
            return True
        elif x < t:
            #lst = lst[:base_idx]
            #lst = list(itertools.islice(lst, 0, base_idx))
            ei = base_idx
            #debug("keep left: %s" % lst)
        else:
            #lst = lst[base_idx+1:]
            #lst = list(itertools.islice(lst, base_idx+1, len(lst)))
            si = base_idx + 1
            #debug("keep right: %s" % lst)
    return False

def binary_search(x:int, lst:list):
    si = 0 # start index
    ei = len(lst) # end index
    while si < ei: # O(1)
        #base_idx = si+pick_base(ei - si)
        base_idx = si + int((ei - si)/2)
        t = lst[base_idx]
        if t == x:
            return True
        elif x < t:
            ei = base_idx
        else:
            si = base_idx + 1
    return False

def get_set4(S:list, T:list):
    #lst = sorted(S)# O(logn)
    C = []
    for t in T:
        if binary_search(t, S):
            C.append(t)
    return C

if __name__ == '__main__':
    S = input_array()
    T = input_array()
    #(n, S, q, T) = input_from_txt(6)
    #print(n, S, q, T)
    ret = get_set4(S, T)
    #ret = get_set2(S, T)
    #ret = get_set(S, T)
    print(len(ret))
