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
    # recursive
    def climbStairs(self, n: int) -> int:
        class Memo:
            def __init__(self):
                self.memo = {}
                self.hits = 0
            def set(self, key, val):
                self.memo[key] = val
            def get(self, key):
                if key in self.memo:
                    self.hits += 1
                    return self.memo[key]
                else:
                    return None
            def has(self, key):
                return key in self.memo
        memo = Memo()
        def step(acc, goal):
            #print("step(%s, %s)" % (acc, goal))
            if memo.has(acc): return memo.get(acc)
            if acc == goal:
                memo.set(acc, 1)
                return 1
            elif acc > goal:
                return 0
            else:
                step1 = step(acc+1, goal)
                step2 = step(acc+2, goal)
                memo.set(acc+1, step1)
                memo.set(acc+2, step2)
                return step1 + step2

        ans = step(0, n)
        #print("hits: %s" % memo.hits)
        #print("hits: %s" % memo.memo)
        return ans


class Solution:
    # iterative
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 2) # buffer
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            if i > 0: dp[i] += dp[i-1]
            if i> 1: dp[i] += dp[i-2]
        return dp[n]



samples = [
    2,
    5
]


for n in samples:
    ans = Solution().climbStairs(n)
    print(ans)