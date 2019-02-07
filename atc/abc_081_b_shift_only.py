#-*- coding: utf-8 -*-
"""
https://qiita.com/drken/items/fd4e5e3630d0f5859067
N=3N=3
　A=(16,12,24)A=(16,12,24)
　答え: 22
"""



def sol(S):
    print(S)
    if all([s%2==0 for s in S]):
        return 1 + sol([int(s/2) for s in S])
    else:
        return 0



cases = [
  (16,12,24),
  (64,64,64,64)
]
for i, (S) in enumerate(cases):
    print("case%s: S:%s" % (i+1, S))
    print(sol(S))
