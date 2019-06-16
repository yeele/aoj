#-*- coding: utf-8 -*-
"""
https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_a
"""

from collections import defaultdict
import sys
def rec2(S):
    if len([s for s in S if s > 0]) == 1:
        return max(S)
    else:
        mini = sys.maxsize
        for i in range(len(S)):
            for j in range(len(S)):
                if i == j: continue
                S2 = []
                for s in S:
                    S2.append(S[j] - S[i])
                mini = min(mini, rec2(S2))
        return mini



def sol2(n, S):
    return rec2(S)


def sol(n, S):

    S.sort()
    mini = min(S)
    maxi = max(S)
    while True:
        sz = len(S)
        if sz < 2 or len(set(S))==1: break
        print("=>S:%s"%S)
        if maxi % mini == 0:
            S.remove(maxi)
            maxi = S[-1]
        else:
            tmp = maxi % mini
            print("tmp:%s" % (tmp))
            S.remove(maxi)
            S.append(tmp)
            S.sort()
            maxi = S[-1]
    print("S:%s"%S)
    return 0 if len(S)==0 else min(S)



#test = False
test = True
if test:
    n = 4
    S = [2, 10, 8, 40]
    #S =list( map(int, "1 6 3".split()))
    print(sol(n, S))

    n = 4
    S = [5, 13, 8, 1000000000]
    #S =list( map(int, "1 6 3".split()))
    print(sol(n, S))

    n = 3
    S = [1000000000, 1000000000, 1000000000]
    print(sol(n, S))

    n = 3
    S = [1, 1, 1]
    print(sol(n, S))

else:
    n = int(input().strip())
    #n, k = map(int, input().split())
    #print("%s %s %s %s" % (type(n), type(k), n, k))
    S =list( map(int, input().split()))
    print(sol(n, S))


