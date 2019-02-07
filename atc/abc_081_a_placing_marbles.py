#-*- coding: utf-8 -*-
"""
https://qiita.com/drken/items/fd4e5e3630d0f5859067
"""



def sol_naive(s):
    ttl = 0
    for c in s:
        if c == "1": ttl+=1
    return ttl


def sol(s):
    ttl = 0
    for c in s:
        if c == "1": ttl+=1
    return ttl

cases = [
    "101",
    "111",
    "000"
]
for i, s in enumerate(cases):
    print("case%s: s:%s" % (i+1, s))
    print(sol(s))
