#-*- coding: utf-8 -*-
"""
https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_a
"""


def sol(n, k):
    ans = int(n/2)+1 if n % 2 == 1 else int(n/2)
    return 'YES' if ans >= k else 'NO'

#test = False
test = True
if test:
    n, k = 3, 2
    #S =list( map(int, "1 6 3".split()))
    print(sol(n, k))

    n, k = 5, 5
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
    n, k = map(int, input().split())
    #S =list( map(int, input().split()))
    print(sol(n, k))


