#-*- coding: utf-8 -*-
"""
https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_a
"""

from collections import defaultdict
def sol(a1, b1, a2, b2, a3, b3):
    S = [a1, b1, a2, b2, a3, b3]
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    if len(d) == 4:
        num2 = 0
        for k, v in d.items():
            if v == 2:
                num2 += 1
        if num2 == 2:
            return 'YES'
    return 'NO'


test = False
test = True
if test:

    print(sol(4, 2, 1, 3, 2, 3))
    print(sol(3, 2, 2,4,1,2))
    print(sol(2,1,3,2,4,3))


    # n, k = 5, 5
    # #S =list( map(int, "7 4 0 3".split()))
    # print(sol(n, k))
    # #
    # n, k = 31, 10
    # #S =list( map(int, "1000000000000".split()))
    # print(sol(n, k))
    #
    # n, k = 10, 90
    # #S =list( map(int, "1000000000000".split()))
    # print(sol(n, k))

else:
    #n, k = map(int, input().split())
    a1, b1 =list( map(int, input().split()))
    a2, b2 =list( map(int, input().split()))
    a3, b3 =list( map(int, input().split()))
    print(sol(a1, b1, a2, b2, a3, b3))


