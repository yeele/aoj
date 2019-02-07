#-*- coding: utf-8 -*-
"""
https://qiita.com/drken/items/fd4e5e3630d0f5859067
  A=2A=2
　B=2B=2
　C=2C=2
　X=100X=100
　答え: 22
"""
dp = {}
def rec(a, b, c, x, ttl, chosen=""):
    #print(a, b, c, x, ttl, "[%s]"%chosen)
    print("number of cache:%s" % len(dp))
    if (a, b, c) in dp: return dp[(a, b, c)]
    ans  = set()
    if a + b + c <= 0:
        if ttl == x:
            ans.add(chosen)
    else:
        if a > 0:
            if ttl+500 <= x: ans.update(rec(a-1, b, c, x, ttl+500, chosen+",500"))
            ans.update(rec(a-1, b, c, x, ttl, chosen))
        if b > 0:
            if ttl+100 <= x: ans.update(rec(a, b-1, c, x, ttl+100, chosen+",100"))
            ans.update(rec(a, b-1, c, x, ttl, chosen))
        if c > 0:
            if ttl+50 <= x: ans.update(rec(a, b, c-1, x, ttl+50, chosen+",50"))
            ans.update(rec(a, b, c-1, x, ttl, chosen))
    #print("returning ans:%s" % (ans))
    dp[(a, b, c)] = ans
    return ans


def sol(a, b, c, x):
    patterns = rec(a, b, c, x, 0)
    print(patterns)
    return len(patterns)


cases = [
    #500, 100, 50
    #(2, 2, 2, 100),
    #(2, 2, 8, 650),
    (2, 2, 10, 650),
]
for i, (S) in enumerate(cases):
    print("case%s: S:%s" % (i+1, S))
    a, b, c, x = S
    print(sol(a, b, c, x))


