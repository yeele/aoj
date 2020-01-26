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

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        if N == 0: return 0
        if N == 1: return cost[0]
        dp = [0] * (N+1) # 10, 15, 20
        dp[0] = 0
        dp[1] = 0  # dp[0, 0, 10, 0]
        for i in range(2, N+1):
            dp[i] = min(
                dp[i-1] + cost[i-1],  # cost:2, 10 + 20 = 30
                dp[i-2] + cost[i-2]   # cost:1, 0 + 15 = 15
            )
        return dp[N]


samples = [
    ([10, 15, 20]),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
]


for S in samples:
    ans = Solution().minCostClimbingStairs(S)
    print(ans)