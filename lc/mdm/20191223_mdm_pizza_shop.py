#-*- coding: utf-8 -*-
from typing import List
import math

import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

import sys
sys.setrecursionlimit(314159265)
from collections import defaultdict

#https://leetcode.com/discuss/interview-question/356935/google-oa-2019-pizza-shop
class Solution:
    def minimumChange(self, P:List[int], O:List[int], X:int) -> int:
        rest = [ X - p for p in P ]
        opt  = [0] * len(P)
        min_idx = -1
        min_val = sys.maxsize
        for option in O:
            for i in range(len(rest)):
                rest[i] -= option
                opt[i] += option
                if min_val > rest[i]:
                    min_val = rest[i]
                    min_idx = i
                if rest[i] == 0:
                    return P[min_idx] + opt[i]
        return P[min_idx] + opt[i]



samples = [
    ([800, 850, 900], [100, 150], 1000, 1000),
]

for P, O, X, expected in samples:
    ans = Solution().minimumChange(P, O, X)
    print(ans)


