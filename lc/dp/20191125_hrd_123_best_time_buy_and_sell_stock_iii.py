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
class Solution:
    #@timeit
    def maxProfit(self, S: List[int]) -> int:
        """
          [7,  1,  5,  3,  6,  4]
        7  0, -6, -2, -2, -1, -1
        1  0,  0,  4,  4,  5,  5
        5
        3
        6
        4
        """
        sz = len(S)
        if sz == 0: return 0
        N_INF = -sys.maxsize
        dp = [[ [N_INF] *  sz for _ in range(sz) ] for _ in range(2)]
        dp = dp[1]
        print(dp)
        def dp_valid(i, j):
            if i < 0 or i >= sz: return False
            if j < 0 or j >= sz: return False
            return True

        def dp_get(dp, i, j, default=N_INF):
            if dp_valid(i, j): return dp[i][j]
            return default

        for i in range(sz):
            for j in range(i, sz):
                profit = S[j] - S[i]
                dp[0][i][j] = max(dp_get(dp[0], i, j), dp_get(dp[0], i, j-1), profit)

        # 2nd time
        for i in range(sz):
            for j in range(i, sz):
                profit = S[j] - S[i]
                dp[0][i][j] = max(dp_get(dp[0], i, j), dp_get(dp[0], i, j-1), profit)

        return dp[sz-1][sz-1]



# 2329pm TLE(time limit exceed)でございます
samples = [
    ([3,3,5,0,0,3,1,4], 6),
    #([1,2,3,4,5], 4),
]


for S, expected in samples:
    ans = Solution().maxProfit(S)
    print(ans)