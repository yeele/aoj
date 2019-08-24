#Definition for singly-linked list.
from typing import List
import sys

import logging
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text1) for _ in range(len(text2))]
        for row in dp:
            logging.debug(row)

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                        if i-1 >=0 and j-1 >=0:
                            dp[i][j] = dp[i-1][j-1] + 1
                        else:
                            dp[i][j] = 1
                else:
                    dp[i][j] = max(
                        0 if i == 0 else dp[i-1][j],
                        0 if j == 0 else dp[i][j-1]
                    )
        return dp[i][j]



samples = [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
]
for text1, text2, expected in samples:
    print("-"*20)
    ans = Solution().longestCommonSubsequence(text1, text2)
    assert ans == expected, "(%s, %s) => %s but %s was expected" % (text1, text2, ans, expected)
    print("(%s, %s) = %s as expected!" % (text1, text2, ans))
