#-*- coding: utf-8 -*-
from typing import List
import logging

#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        M = 3
        N = len(nums)
        dp = [[0] * N for _ in range(M)]
        idx = [([[]] * N) for _ in range(M)]
        # edge case
        if len(nums) < (k * M): return ans
        for row in idx: print(idx)
        return
        for m in range(M):
            for n in range(N):
                if n >= m * k:
                    new_val = sum(nums[n-k+1:n+1]) + dp[m-1][n-k]
                    pre_val = dp[m][n-1]
                    if new_val > pre_val:
                        # update
                        dp[m][n] = sum(nums[n-k+1:n+1]) + dp[m-1][n-k]
                        idx[m][n] = [n-k+1]
                    else:
                        dp[m][n] = dp[m][n-1]



        # for row in dp: print(row)
        # print(m, n)

        return dp[m][n]



samples = [
    ([1,2,1,2,6,7,5,1], 2, [0, 3, 5]),
]

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
for S, k ,expected in samples:
    ans = Solution().maxSumOfThreeSubarrays(S, k)
    print(ans)
