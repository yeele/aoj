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
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = sys.maxsize
        maxi = None
        max_diff = 0
        for price in prices:
            if price < mini:
                mini = price
                maxi = price
            else:
                mini = min(mini, price)
                maxi = max(maxi, price)
            #print("maxi:%s, mini:%s" % (maxi, mini))
            max_diff = max(max_diff, maxi - mini)
        return max_diff


samples = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
]


for S, expected in samples:
    ans = Solution().maxProfit(S)
    print(ans)