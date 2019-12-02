#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""




class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        dp[i][j] = i番目までとj番目までの文字はinterleaving かどうか？
        aabcc, abbca => aadbbcbcac

        aab abb => aadbb
        """
        sz1 = len(s1)
        sz2 = len(s2)
        sz3 = len(s3)
        if (sz1 + sz2) != sz3: return False
        if sz3 == 0: return True
        dp = [[False]*(sz1+1) for _ in range(sz2+1)]
        for i in range(sz2+1):
            if i > 0 and s3[i - 1] == s2[i-1]:
                dp[i][0] = True
        for j in range(sz1+1):
            if j > 0 and s3[j - 1] == s1[j-1]:
                dp[0][j] = True

        # for row in dp: print(row)
        # print("-"*20)
        for i in range(1, sz2+1):
            for j in range(1, sz1+1):
                if s3[i + j - 1] == s1[j-1] and s3[i + j - 1] == s2[i-1]:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif s3[i + j - 1] == s1[j-1]:
                    dp[i][j] = dp[i][j-1]
                elif s3[i + j - 1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j]
        # print("-"*20)
        # for row in dp: print(row)
        return dp[i][j] and (dp[0][1] or dp [1][0])

samples = [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "a", False),
    # # 89 / 101 test cases passed.
    # # https://leetcode.com/submissions/detail/280064502/
    # # by TLE
    # # @20191201 2045pm
    # # 84 / 101 test cases passed.
    ("aabc", "abad", "aabadabc", True),
    # # """
    # # 0 1 2 3 4 5 6 7
    # # a a b a d a b c
    # #   _ a a b c
    # # _   t t t f
    # # a t t
    # # b f
    # # a f
    # # d f
    # # """
    # # @2052pm
    # # # 100 / 101 test cases passed.
    ("db", "b", "cbb", False),
]
for S1, S2, S3, expected in samples:
    print("-"*20)
    ans = Solution().isInterleave(S1, S2, S3)
    print("(%s) = %s as expected!" % (ans, expected))

