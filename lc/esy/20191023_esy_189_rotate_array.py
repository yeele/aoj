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
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmps = []
        sz = len(nums)
        if k > sz:
            k = k % sz
        #print("k:%s, %s %s %s" % (k, sz-1, sz-1-k, -1))
        for i in range(sz-1, sz-1-k, -1):
            tmps.append(nums[i])
        for i in range(sz - k -1, -1, -1):
            #print("%s <- %s" % (i+k, i))
            nums[i+k] = nums[i]
        i = 0
        while len(tmps) > 0:
            x = tmps.pop()
            nums[i] = x
            i += 1



samples = [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ([-1], 2, []),
]


for S, k, expected in samples:
    ans = Solution().rotate(S, k)
    print(S)