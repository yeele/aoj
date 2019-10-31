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
from collections import defaultdict

class Solution:
    def longestOnes(self, S: List[int], k: int) -> int:
        maxi = 0
        sz = len(S)
        i = j = 0
        while i < sz and j < sz:
            if S[j] == 1:
                maxi = max(maxi, j+1 - i)
                j += 1
            else:
                if k > 0:
                    maxi = max(maxi, j+1 - i)
                    k -= 1
                    j += 1
                else:
                    if S[i] == 0:
                        k += 1
                    i += 1
        return maxi


# 完敗。手足でず。。。。


samples = [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
]

for S, k, expected in samples:
    ans = Solution().longestOnes(S, k)
    print(ans)
