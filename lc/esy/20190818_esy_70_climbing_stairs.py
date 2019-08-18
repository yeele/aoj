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

class Solution_timeexceeded:
    def rec(self, cur, n):
        if cur == n:
            return 1
        elif cur > n:
            return 0
        else:
            return self.rec(cur+1, n) + self.rec(cur+2, n)

    @timeit
    def climbStairs(self, n: int) -> int:
        return self.rec(0, n)

from collections import defaultdict
class Solution:
    def __init__(self):
        self.cache = defaultdict(int)

    def rec(self, cur, n):
        if cur in self.cache: return self.cache[cur]
        if cur == n:
            self.cache[cur] = 2
            return 1
        elif cur > n:
            return 0
        else:
            step1 = self.rec(cur+1, n)
            self.cache[cur+1] = step1
            step2 = self.rec(cur+2, n)
            self.cache[cur+2] = step2
            return step1 + step2

    @timeit
    def climbStairs(self, n: int) -> int:
        self.cache = defaultdict(int)
        return self.rec(0, n)

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(5))
print(Solution().climbStairs(35))



