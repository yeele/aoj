#-*- coding: utf-8 -*-
"""
"""

import time
def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        print('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper

"""
考えるポイント
最初、俺はchosenに選んだ札を覚えておくことを考えた。
でも、後で合計金額を覚えておく方が、軽いし、良いと考えた。
抽出は、再起の持ち越しはなるだけ楽な形で、記憶できないか？と考えること。

あ、でもこの場合は、選んだパターンを残しておおかないといけなかった。とほほ。

"""


"""
グゲ、再起の上限に達してしまった。
RecursionError: maximum recursion depth exceeded in comparison
再起の数は1000を越えるときは、イテレーティブに書かなくてわ。
or
import sys
sys.setrecursionlimit(10000)
"""


import sys
sys.setrecursionlimit(10000)
def rec(n, i, chosen):
    ttl = chosen[0]*10000 + chosen[1]*5000 + chosen[2]*1000
    if ttl == y:
        return [chosen]
    elif i == n:
        return []
    else:
        ans = []
        A = chosen.copy()
        A[0] += 1
        ans += rec(n, i+1, A)
        if len(ans) > 0: return ans
        B = chosen.copy()
        B[1] += 1
        ans += rec(n, i+1, B)
        if len(ans) > 0: return ans
        C = chosen.copy()
        C[0] += 1
        ans += rec(n, i+1, C)
        return ans


def iterative(n):
    Ys = int(y / 1000)
    dp = [[0] * n for _ in range(Ys)]
    for i in range(Ys):
        for j in range(n):
            for bill in (10000, 5000, 1000):
                goal = 1000 * (n+1)
                # oh, no, let me take a rest


@deco
def sol(n, y):
    for a in range(n):
        for b in range(n-i):
            c = n - (a+b)
            ttl = 10000*a + 5000*b + 1000*c
            if ttl == y:
                return (a, b, c)


@deco
def sol_rec(n, y):
    # mCn + oCn + n-(m+o)Cn
    chosen = [0, 0, 0]
    answers = rec(n, 0, chosen)
    if len(answers) > 0:
        return answers[0]





"""
N=9
Y=45000
(4,0,5)
"""
from collections import defaultdict
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

cases = [
    #(9, 45000),
    (2000, 6000000)
]
for i, (S) in enumerate(cases):
    print("case%s: S:%s" % (i+1, S))
    n, y = S
    print(sol(n, y))


