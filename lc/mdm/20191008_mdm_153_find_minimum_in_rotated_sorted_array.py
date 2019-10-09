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
    def findMin(self, nums: List[int]) -> int:
        sz = len(nums)
        assert(sz > 0) # Assumption. len(nums) > 0
        mini = sys.maxsize
        for i in range(len(nums)):
            mini = min(mini, nums[i])
        return mini


# 2159pm start
# 2205pm implemented
samples = [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
]

for S, expected in samples:
    ans = Solution().findMin(S)
    print(ans)