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
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return nums
        pre = nums[0]-1
        ini = nums[0]
        ans = []
        for n in nums:
            if n - 1 == pre:
                pass
            else:
                tmp = "%s->%s" % (ini, pre)
                ans.append(tmp)
                ini = n
            pre = n
        if ini == pre:
            tmp = "%s" % (ini)
        else:
            tmp = "%s->%s" % (ini, pre)
        ans.append(tmp)

        return ans

samples = [
    ([0,1,2,4,5,7], ["0->2","4->5","7"]),
]

for S, expected in samples:
    ans = Solution().summaryRanges(S)
    print(ans)


