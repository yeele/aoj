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
        j = 0 # write pointer
        if nums == None or len(nums) == 0: return 0
        pre = None
        dup = 0
        for i in range(len(nums)):
            if nums[i] == pre: # duplicate
                dup += 1
                nums[j] = nums[i]
                if dup < 2:
                    j+=1
            else:
                dup = 0
                nums[j] = nums[i]
                j+=1
            pre = nums[i]
        return j

samples = [
    #[1,1,1,2,2,3],
    [0,0,1,1,1,1,2,3,3],
]


for sample in samples:
    ans = Solution().removeDuplicates(sample)
    print("ans:%s" % ans)
    print("new array: %s" % sample[:ans])


