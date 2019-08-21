#Definition for singly-linked list.
from typing import List
import sys

class Solution_close_but_not_solved:

    def coinChange(self, S: List[int], k: int) -> int:
        import logging
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")

        if k <= 0: return 0
        dp = [ [0] * k for _ in range(len(S)) ]
        for row in dp:
            logging.debug(row)
        minis = [sys.maxsize] * len(S)

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                coin = S[i]
                if i == 0:
                    if (j + 1) % coin == 0:
                        dp[i][j] = int((j + 1) / coin)
                    else:
                        dp[i][j] = -1
                else:
                    if i - 1 >= 0 and (j - coin) >= 0:
                        this = dp[i-1][j-coin] + 1
                    else:
                        this = sys.maxsize

                    if i >= 0 and (j - coin) >= 0:
                        that = dp[i][j-coin] + 1
                    else:
                        that = sys.maxsize
                    dp[i][j] = min(this, that)

                minis[i] = min(minis[i], dp[i][j])

        for row in dp:
            logging.debug(row)
        return minis[i]


class Solution:
    def coinChange(self, S: List[int], k: int) -> int:
        import logging
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")

        if k <= 0 or S is None or len(S) == 0: return 0
        dp = [ [0] * k for _ in range(len(S)) ]
        # for row in dp:
        #     logging.debug(row)
        MAXN = sys.maxsize
        #MAXN = 100

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                coin = S[i]
                if i == 0:
                    if (j + 1) % coin == 0:
                        dp[i][j] = int((j + 1) / coin)
                    else:
                        dp[i][j] = MAXN
                else:
                    if i >= 0 and (j - coin) >= 0:
                        that = dp[i][j-coin] + 1
                    else:
                        if coin == j+1: that = 1
                        else: that = MAXN
                    dp[i][j] = min(that, dp[i-1][j])

        for row in dp:
            logging.debug(row)

        return -1 if dp[i][j] == MAXN else dp[i][j]


samples = [
    # ([1, 2, 5], 11),
    # ([1, 2, 5], 53),
    # ([1], 0),
    # ([1,2147483647], 2),
    # ([1,3,5], 7),
    # ([1, 2], 2),
    ([2,5,10,1], 27),
]
for S, k in samples:
    print("-"*20)
    ans = Solution().coinChange(S, k)
    print("%s, %s = %s" % (S, k, ans))
