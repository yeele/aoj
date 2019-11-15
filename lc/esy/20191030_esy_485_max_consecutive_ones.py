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
class Solution_ok:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = local = 0
        for n in nums:
            if n == 1:
                local += 1
                maxi = max(maxi, local)
            else:
                local = 0
        return maxi


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding window solution
        maxi = local = 0
        i = j = 0
        sz = len(nums)
        while j < sz:
            if nums[j] == 1:
                local += 1
                maxi = max(maxi, local)
                j+=1
            else:
                local = 0
                i = j + 1
                j = i

        return maxi

samples = [
    ([1,1,0,1,1,1], 3),
]


for S, expected in samples:
    ans = Solution().findMaxConsecutiveOnes(S)
    print(ans)