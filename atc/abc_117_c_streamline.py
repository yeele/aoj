#-*- coding: utf-8 -*-
"""
https://atcoder.jp/contests/abc117/tasks/abc117_a
"""

def sol(n, S):
    if S is None or len(S) == 0: return 0
    S.sort() # sort in place
    #print(S)
    diffs = []
    pre = S[0]
    for i in range(1, len(S)):
        diffs.append(S[i] - pre)
        pre = S[i]
    diffs.sort(reverse=True)
    #print(diffs)
    for x in range(n-1):
        if len(diffs) > 0:
            del diffs[0]
    return sum(diffs)



test = True
if test:
    n, m = 2, 5
    S =list( map(int, "10 12 1 2 14".split()))
    print(sol(n, S))

    n, m = 3, 7
    S =list( map(int, "-10 -3 0 9 -100 2 17".split()))
    print(sol(n, S))

    n, m = 100, 1
    S =list( map(int, "-100000".split()))
    print(sol(n, S))


else:
    n, m = map(int, input().split())
    S =list( map(int, input().split()))
    #print(n, S)
    print(sol(n, S))


