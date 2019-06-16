#-*- coding: utf-8 -*-
"""
https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_a
"""


def sol(a, b):
    if b % a == 0: return a+b
    else: return b-a


test = False
test = True
if test:
    n, k = 4, 12
    #S =list( map(int, "1 6 3".split()))
    print(sol(n, k))

    n, k = 8, 20
    #S =list( map(int, "7 4 0 3".split()))
    print(sol(n, k))
    #
    n, k = 31, 10
    #S =list( map(int, "1000000000000".split()))
    print(sol(n, k))

    n, k = 10, 90
    #S =list( map(int, "1000000000000".split()))
    print(sol(n, k))

else:
    a, b = map(int, input().split())
    #S =list( map(int, input().split()))
    print(sol(a, b))


