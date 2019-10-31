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
    def findLHS(self, nums: List[int]) -> int:
        # space O(N) - duplicate
        mapping = defaultdict(int)
        # time O(N)
        for n in nums:
            mapping[n] += 1
        # time O(N)
        maxi = 0
        pre = None
        tups = [(n, count) for n, count in mapping.items()]
        tups.sort(key=lambda tup: tup[0])
        for n, count in tups:
            print(n, count)
            if pre is not None and abs(pre - n) == 1:
                y = mapping[n] + mapping[pre]
                maxi = max(maxi, y)
            pre = n

        return maxi


samples = [
    ([1,3,2,2,5,2,3,7], 5),
    # 20 mins elapsed
    # 69/201 failed https://leetcode.com/submissions/detail/272964580/
    ([1, 1, 1, 1], 0),
    # 22 mins elapsed
    # 100 / 201 test cases passed.
    ([0,3,1,3,3,3,0,1,0,2,0,3,1,3,-3,2,0,3,1,2,2,-3,2,2,3,3], 15),
    # solved by sortting
    # 25 mins elapased...
    # 190 / 201 test cases passed.
    ([0,3,0,0,1,1,1,3,1,3,2,3,2,3,-1,0,2,1,0,0,0,1,3,3,-3,3,3,1,3], 14),
    # Becareful with if pre, Dont go through even in pre == 0 case, unexpectedlly.


]


for S, expected in samples:
    ans = Solution().findLHS(S)
    print(ans)