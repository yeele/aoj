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
    def numTrees(self, n: int) -> int:

        if n <= 2: return n
        dp = [0 for i in range(n+1)]
        dp[1] = 1; dp[2] = 2;

        for i in range(3, n+1):
            tmp = 0
            for j in range(i):
                left = j
                right = i - j -1
                if left == 0: tmp += dp[right]
                elif right == 0: tmp += dp[left]
                else: tmp += dp[left] * dp[right]
            dp[i] = tmp
        return dp[n]


samples = [
    #1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845,
    # (0, 0),
    # (1, 1),
    # (2, 2),
    (3, 5),
    (4, 14),
    (5, 42),
]

for S, expected in samples:
    ans = Solution().numTrees(S)
    print(ans)