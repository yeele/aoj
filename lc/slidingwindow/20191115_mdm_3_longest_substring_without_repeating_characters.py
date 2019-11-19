#-*- coding: utf-8 -*-
from typing import List
import math

import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

import sys
sys.setrecursionlimit(314159265)

class Solution:
    def lengthOfLongestSubstring(self, S: str) -> int:
        if S is None or len(S) == 0: return 0
        sz = len(S)
        l = 0
        r = 1
        maxi = 1
        while l < sz and r < sz:
            #print("l -> %s, r -> %s" % (l, r))
            if S[r] in S[l:r]:
                # move l until  non overlap point
                while S[l] != S[r]:
                    l += 1
                l += 1
            else:
                maxi = max(maxi, r - l + 1)
                # move r +1
                r += 1
        return maxi


samples = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]


for S, expected in samples:
    ans = Solution().lengthOfLongestSubstring(S)
    print(ans)