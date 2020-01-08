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
    def minPathSum(self, grid: List[List[int]]) -> int:
        """

        """
        if grid is None or len(grid) == 0 or len(grid[0])==0: return None
        m = len(grid[0])
        n = len(grid)
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                up = dp[i-1][j] if i >= 1 else None
                left = dp[i][j-1] if j >= 1 else None
                curr = grid[i][j]
                if up is not None and left is not None: path = min(up, left)
                elif up is not None: path = up
                elif left is not None: path = left
                else:
                    path = 0
                dp[i][j] = path + curr
                # print("min({}, {}) + grid[{}][{}] {}), dp[{}][{}] {}".
                #       format(up, left, i, j, grid[i][j], i, j, dp[i][j]))
        #for row in dp: print(row)
        return dp[i][j]


samples = [
    # (
    #     [
    #         [1,3,1],
    #         [1,5,1],
    #         [4,2,1]
    #     ], 7
    # ),
    (
        [[0,2,2,6,4,1,6,2,9,9,5,8,4,4],[0,3,6,4,5,5,9,7,8,3,9,9,5,4],[6,9,0,7,2,2,5,6,3,1,0,4,2,5],[3,8,2,3,2,8,8,7,5,9,6,3,4,5],[4,0,1,3,9,2,0,1,6,7,9,2,8,9],[6,2,7,9,0,9,5,2,7,5,1,4,4,7],[9,8,3,3,0,6,8,0,8,8,3,5,7,3],[7,7,4,5,9,1,5,0,2,2,2,1,7,4],[5,1,3,4,1,6,0,4,3,8,4,3,9,9],[0,6,4,9,4,1,5,5,4,2,5,7,4,0],[0,1,6,6,4,9,2,7,8,2,1,3,3,7],[8,4,9,9,2,3,8,6,6,5,4,1,7,9]],
        63
    )
]

for S, expected in samples:
    ans = Solution().minPathSum(S)
    print(ans)
