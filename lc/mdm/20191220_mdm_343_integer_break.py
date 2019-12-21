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

from functools import lru_cache

class Solution_discuss:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n <= 0 :
                return 0
            elif n == 1:
                return 1
            res = n
            for i in range(1, n // 2 + 1):
                res = max(res, i * dp(n - i))
            print("dp(%s) = %s" % (n, res))
            return res

        return max(dp(n - i) * i for i in range(1, n))


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        5 + 5
        1 + 9
        2 + 8
        3 + 7
        3 + 3 + 4
        """
        dp = [0] * (n+3)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2

        if n <= 3: return dp[n]

        for i in range(4, n+1):
            for j in range(1, i // 2 + 1):
                right = i-j
                dp[i] = max(dp[i], j * dp[right], j * right)
            print(dp)
        return dp[n]

samples = [
    (2, 1),
    (10, 36),
]

for n, expected in samples:
    ans = Solution().integerBreak(n)
    print(ans)
