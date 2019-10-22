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
    def numTrees(self, n: int) -> int:
        return 0


samples = [
    ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
]

for S, expected in samples:
    #ans = Solution().threeSum(S)
    ans = Solution().numTrees(S)
    #print(ans)