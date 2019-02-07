#-*- coding: utf-8 -*-
"""
https://qiita.com/drken/items/fd4e5e3630d0f5859067
1≤a,b≤100001≤a,b≤10000
aa, bb は整数
【数値例】
1)
　a=3a=3
　b=4b=4
　答え: Even
"""



def sol(a, b):
    return "EVEN" if (a * b) % 2 == 0 else "ODD"


cases = [
    (3, 4),
    (3, 3),
    (1, 0)
]
for i, (a, b) in enumerate(cases):
    print("case%s: a:%s, b:%s" % (i+1, a, b))
    print(sol(a, b))
