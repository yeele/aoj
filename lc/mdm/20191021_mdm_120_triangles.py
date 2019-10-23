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

class Solution_2SquaredByNSolution:
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


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0: return 0
        m = len(triangle[n-1])
        dp = [0 for _ in range(m+1)]
        print(dp)
        for i in range(m-1, -1, -1):
            for j, x in enumerate(triangle[i]):
                dp[j] = min(x + dp[j], x + dp[j+1])
        return dp[0]

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
