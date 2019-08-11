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

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1 # write pointer
        if nums == None or len(nums) == 0: return 0
        pre = nums[0]
        dup = 0
        dup_pre = None
        for i, x in enumerate(nums):
            if i == 0:
                pass
            elif x == pre: # duplicate
                if x != dup_pre:
                    dup += 1
                dup_pre = x
            else:
                nums[j] = x
                j+=1
            pre = x
        return j

samples = [
    [1, 1, 2],
    [0,0,1,1,1,2,2,3,3,4],
    [0, 0, 0, 0],
    [0, 1, 2, 3, 4],
]


for sample in samples:
    ans = Solution().removeDuplicates(sample)
    print("ans:%s" % ans)
    print("new array: %s" % sample[:ans])


