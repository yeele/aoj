#Definition for singly-linked list.
from typing import List
import sys

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass



samples = [
    ("abcde", "ace", 3),
]
for text1, text2, expected in samples:
    print("-"*20)
    ans = Solution().longestCommonSubsequence(text1, text2)
    assert ans == expected, "(%s, %s) => %s but %s was expected" % (text1, text2, ans, expected)
    print("(%s, %s) = %s as expected!" % (text1, text2, ans))
