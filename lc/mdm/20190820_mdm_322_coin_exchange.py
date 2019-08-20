#Definition for singly-linked list.
from typing import List
import sys


class Solution:
    def coinChange(self, S: List[int], k: int) -> int:
        import logging
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        if k <= 0: return 0
        dp = [ [0] * k for _ in range(len(S)) ]
        for row in dp:
            logging.debug(row)
        mini = sys.maxsize

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                coin = S[i]
                if i == 0:
                    if (j + 1) % coin == 0:
                        dp[i][j] = int((j + 1) / coin)
                    else:
                        dp[i][j] = -1
                    if j == k-1:
                        #if dp[i][j] < mini: print("updated!! dp[%s][%s]:%s < mini:%s" % (i, j, dp[i][j], mini))
                        mini = min(mini, dp[i][j])
                else:
                    if i - 1 >= 0 and (j - coin) >= 0:
                        #print("dp[%s][%s]" % (i-1, j-coin))
                        this = dp[i-1][j-coin] + 1
                    else:
                        #print("...")
                        this = sys.maxsize

                    if i >= 0 and (j - coin) >= 0:
                        that = dp[i][j-coin] + 1
                    else:
                        #print(",,,")
                        that = sys.maxsize

                    dp[i][j] = min(this, that)
                    if j == k-1:
                        #if dp[i][j] < mini: print("updated!! dp[%s][%s]:%s < mini:%s" % (i, j, dp[i][j], mini))
                        mini = min(mini, dp[i][j])

        for row in dp:
            logging.debug(row)
        return mini


samples = [
    ([1, 2, 5], 11),
    # ([1, 2, 5], 53),
    # ([1], 0),
    # ([1,2147483647], 2),
    # ([1,3,5], 7),
]
for S, k in samples:
    ans = Solution().coinChange(S, k)
    print("%s, %s = %s" % (S, k, ans))
