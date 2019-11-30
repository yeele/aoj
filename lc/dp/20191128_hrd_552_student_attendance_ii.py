#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

class Solution:
    def checkRecord(self, n: int) -> int:
        cost = [
            0, # P
            0.5, # L
            1, # A
            1.5, # -
        ]
        if n == 0: return 0
        if n == 1: return 3
        if n == 2: return 8
        dp = [[0] * n for _ in range(len(cost))]
        for i in range(n):
            dp[0][i] = 1
        dp[1][0] = 2
        dp[2][0] = 3
        dp[3][0] = 0
        # --- second
        dp[1][1] = 3
        dp[2][1] = 6
        dp[3][1] = 8
        """
        """
        for i in range(1, len(cost)):
            for j in range(2, n):
                # print("_"*20)
                # for row in dp: print(row)
                up = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = up + left

        #for row in dp: print(row)
        return dp[i][j] % (10**9 + 7)

samples = [
    (2, 8),
    (3, 8),
    (4, 8),
]
for N, expected in samples:
    print("-"*20)
    ans = Solution().checkRecord(N)
    print("(%s) = %s as expected!" % (ans, expected))

