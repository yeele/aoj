#-*- coding: utf-8 -*-
from typing import List
import logging
import re
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        M = 3
        N = len(nums)
        dp = [[0] * N for _ in range(M)]
        idx = [[''] * N for _ in range(M)]

        # edge case
        if len(nums) < (k * M): return ans


        for m in range(M):
            sum_win = None
            for n in range(N):
                if n >= m * k:
                    #sum_win = sum(nums[n-k+1:n+1])
                    if sum_win is None:
                        sum_win = sum(nums[n-k+1:n+1])
                    else:
                        if n-k >= 0:
                            sum_win += (nums[n] - nums[n-k])
                        else:
                            sum_win = sum(nums[n-k+1:n+1])
                    new_val = sum_win + dp[m-1][n-k]
                    pre_val = dp[m][n-1]
                    if new_val > pre_val:
                        # update
                        dp[m][n] = sum_win + dp[m-1][n-k]
                        if len(idx[m-1][n-k]) > 0:
                            idx[m][n] = idx[m-1][n-k] + "," + "%s" % str(n-k+1)
                        else:
                            idx[m][n] = "%s" % str(n-k+1)
                    else:
                        dp[m][n] = dp[m][n-1]
                        idx[m][n] = idx[m][n-1]

        #for row in idx: print(row)
        # for row in dp: print(row)
        # print(m, n)

        #return dp[m][n]
        tmp = idx[m][n]
        #return [ int(x.strip()) for x in tmp.split(',') if x.strip() != ""]
        return eval("[%s]" % re.sub(",+", ',', tmp))



samples = [
    #([1,2,1,2,6,7,5,1], 2, [0, 3, 5]),
    ([1,2,1,2,2,2,2,2], 2, [0, 3, 5]),
    # TLE 39/42 test
    # https://leetcode.com/submissions/detail/287759175/testcase/
]

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
for S, k ,expected in samples:
    ans = Solution().maxSumOfThreeSubarrays(S, k)
    print(ans)
