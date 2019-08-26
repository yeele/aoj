#Definition for singly-linked list.
from typing import List
import sys

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def wordBreak_correct(self, s, wordDict):
        input_sz = len(s)
        dp = [[0] * (input_sz) for _ in range(input_sz)]
        def get_dp(i, j, d):
            if i < 0 or i > input_sz: return d
            if j < 0 or j > input_sz: return d
            return dp[i][j]

        for i in range(input_sz):
            for j in range(input_sz):
                if s[i:j+1] in wordDict:
                    sz = j+1-i
                    pj = j-sz
                    dp[i][j] = max(min(1, get_dp(i, pj, 1)), get_dp(i-1, j, 0))
                    if j == input_sz-1 and dp[i][j] == 1: return True
                else:
                    dp[i][j] = max(0, get_dp(i-1, j, 0))
        return dp[-1][-1] == 1

    def wordBreak(self, S: str, D: List[str]) -> bool:
        dp = [ [0] * len(S) for _ in range(len(S)) ]
        length = len(S)
        def L(i, j, default=0):
            if i < 0 or i >= length: return default
            if j < 0 or j >= length: return default
            return dp[i][j]
        def L_print():
            for row in dp:
                logging.debug(row)

        for i in range(length):
            for j in range (length):
                if S[i:j+1] in D:
                    sz = j+1-i
                    dp[i][j] = max(min(1, L(i,j - sz, default=1)), L(i-1,j))
                    #dp[i][j] = max(L(i, j-sz, 1), L(i-1, j)) # これだと、j-szが, 0のパターンで間違い
                else:
                    dp[i][j] = L(i-1,j)

                if j == len(S)-1 and dp[i][j] == 1: return True
        return True if dp[i][j] == 1 else False


samples = [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("aaaaaaa", ["aaaa","aaa"], True),
]
for S, D, expected in samples:
    print("-"*20)
    ans = Solution().wordBreak(S, D)
    assert ans == expected, "(%s, %s) => %s but %s was expected" % (S, D, ans, expected)
    print("(%s, %s) = %s as expected!" % (S, D, ans))
