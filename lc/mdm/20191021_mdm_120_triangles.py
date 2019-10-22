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

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def rec(S, j, i, sofar=0): # j is previous
            if i > len(S):
                return sofar
            # choose
            ans1 = rec(S, i, i+1, sofar+S[i][j])
            # choose
            ans2 = rec(S, i, i+1, sofar+S[i][j+1])
            return min(ans1, ans2)

        return rec(triangle, 0, 0, 0)


samples = [
    (
        [
            [2],
            [3,4],
            [6,5,7],
            [4,1,8,3]
        ],
        None
    )
]

for S, expected in samples:
    #ans = Solution().threeSum(S)
    ans = Solution().minimumTotal(S)
    print(ans)
