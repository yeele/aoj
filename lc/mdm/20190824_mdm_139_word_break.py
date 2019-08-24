#Definition for singly-linked list.
from typing import List
import sys

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def wordBreak(self, S: str, D: List[str]) -> bool:
        L = [ [0] * len(S) for _ in range(len(S)) ]
        for i in range(len(S)):
            for j in range (0, len(S)):
                if j < i:
                    if i - 1 >= 0:
                        L[i][j] = L[i-1][j] # 伝搬
                    continue
                logging.debug("checking S[%s:%s] = %s, sz = %s" % (i, j, S[i:j+1], j+1-i))
                if S[i:j+1] in D:
                    sz = j+1-i
                    if j - sz >= 0:
                        L[i][j] = L[i][j- sz]
                    else:
                        L[i][j] = 1
                else:
                    if i -1 >= 0:
                        L[i][j] = L[i-1][j]
                for row in L:
                    logging.debug(row)
                if j == len(S)-1 and L[i][j] == 1: return True
        for row in L:
            logging.debug(row)
        return True if L[i][j] == 1 else False


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
