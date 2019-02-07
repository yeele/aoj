#-*- coding: utf-8 -*-
"""
https://atcoder.jp/contests/abc117/tasks/abc117_a
"""

def sol(n, S):
    maxi = max(S)
    ttl = sum(S)
    others = ttl - maxi
    print('Yes' if maxi < others else 'No')

test = False
if test:
    n = 4
    S =list( map(int, "3 8 5 1".split()))
    sol(n, S)

    n = 4
    S =list( map(int, "3 8 4 1".split()))
    sol(n, S)

    n = 10
    S =list( map(int, "1 8 10 5 8 12 34 100 11 3".split()))
    sol(n, S)


else:
    n = int(input())
    S =list( map(int, input().split()))
    #print(n, edges)
    sol(n, S)


