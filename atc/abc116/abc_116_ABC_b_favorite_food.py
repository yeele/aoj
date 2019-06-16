#-*- coding: utf-8 -*-
"""
https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_a
"""

from collections import defaultdict
def sol(n, m, Ss):
    stack = defaultdict(int)
    all_like = 0

    for S in Ss:
        #print("S: %s," % S)
        for i, s in enumerate(S):
            if i == 0: continue
            #print("i:%s, s:%s" % (i, s))
            stack[s] += 1
            #print("stack: %s" % stack)
            if stack[s] == n:
                all_like +=1
    return all_like



#test = False
test = True
if test:
    n, k = 3, 4
    Ss = [
        [2, 1, 3],
        [3, 1, 2, 3],
        [2, 3, 2]
    ]
    #S =list( map(int, "1 6 3".split()))
    print(sol(n, k, Ss))


else:
    n, k = map(int, input().split())
    #print("%s %s %s %s" % (type(n), type(k), n, k))
    Ss = []
    for i in range(n):
        S =list( map(int, input().split()))
        Ss.append(S)
    print(sol(n, k, Ss))


