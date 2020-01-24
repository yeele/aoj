#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        max_w = max([ tup[1] for tup in courses ])
        N = len(courses)
        dp = [[0] * max_w for _ in range(N)]
        def dp_valid(i, j):
            if i < 0 or i >= N: return False
            if j < 0 or j >= max_w: return False
            return True
        def DP(i, j):
            if dp_valid(i, j): return dp[i][j]
            else: return 0

        # [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
        for i in range(N):       # iは商品どれ
            for j in range(max_w): # jは現在の重さ
                constrain = courses[i][1]
                if j <= constrain: a = DP(i-1, j-courses[i][0]) + 1
                else: a = DP(i-1, j)
                b = DP(i, j-1)
                dp[i][j] = max(a, b)

        return dp[i][j]


samples = [
    ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]),
]
for S in samples:
    print("-"*20)
    ans = Solution().scheduleCourse(S)
    print("(%s) = %s as expected!" % (S, ans))





