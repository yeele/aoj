#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

from collections import defaultdict
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        memo = [-1] * len(T)
        mini = sys.maxsize
        maxi = -sys.maxsize
        ans = S
        index_helper = defaultdict(lambda:-1)
        for i, c in enumerate(T):
            index_helper[c] = i
        counter = 0
        for i, c in enumerate(S):
            idx = index_helper[c]
            if idx == -1: continue # T以外のキャラ

            local = max(i, memo[idx])
            if memo[idx] == -1:
                counter+=1 # 初めて見つかったということで。
            memo[idx] = max(memo[idx], local)
            # mini = min(mini, local)
            # maxi = max(maxi, local) # こっちのが高速だが間違ってるのでまずは。
            mini = min(memo) # O(T)なんんで、これだとO(N)に届かずRTEくらいそう
            maxi = max(memo)
            if counter == len(T):
                if (maxi+1) - mini < len(ans):
                    ans = S[mini:maxi+1]
        return ans




samples = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "aa", ""),
]
for S, T, expected in samples:
    print("-"*20)
    ans = Solution().minWindow(S, T)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (S, T, ans, expected)
    print("(%s, %s) = %s as expected!" % (S, T, ans))
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    #print("(%s) = %s as expected!" % (S, ans))

