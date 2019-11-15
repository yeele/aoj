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
    def integerReplacement(self, n: int) -> int:


        def rec(n, counter):
            #print("%s ~> " % n, end="")
            if n == 1:
                return counter
            else:
                if n % 2 == 0:
                    # O(logN)
                    return rec(n/2, counter+1)
                else:
                    local2 = rec(n+1, counter+1)
                    local3 = rec(n-1, counter+1)
                    return min(local2, local3)

        return rec(n, 0)




samples = [
    (8, 3),
    # 8 -> 4 -> 2 -> 1
    (7, 4),
    #Explanation:
    #7 -> 8 -> 4 -> 2 -> 1 or
    #7 -> 6 -> 3 -> 2 -> 1
    (100, None),
    (10000000, None),
]

for n, expected in samples:
    ans = Solution().integerReplacement(n)
    print(ans)
