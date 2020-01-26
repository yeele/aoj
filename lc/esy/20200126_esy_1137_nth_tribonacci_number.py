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
    def tribonacci(self, n: int) -> int:
        import collections
        dp = collections.deque([0, 1, 1]);
        last2 = 1 + 1
        total = 0 + 1 + 1
        t0_1 = 1
        t2 = 1
        if n <= 1: return n
        if n == 2: return 1
        if n == 3: return 2
        for i in range(4, n+2):
            t3 = t0_1 + t2
            t0 = dp.popleft()
            t0_1 = t3 - t0
            t2 = t3
            dp.append(t3)
        print(dp)
        return t3


    def tribonacci_iter(self, n: int) -> int:
        #dp = {0:0,1:1,2:1}
        #dp = [0] * (n + 3)
        #dp[0] = 0; dp[1] = 1; dp[2] = 1;
        import collections
        if n <= 1: return n
        if n == 2: return 1
        t0 = 0; t1 = 1; t2 = 1
        for i in range(3, n+1):
            t3 = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t3
        return t3

    def tribonacci_rec(self, n: int) -> int:
        memo = {0:0,1:1,2:1}
        def f(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n == 1 or n==2: return 1
            a = f(n-1)
            b = f(n-2)
            c = f(n-3)
            #memo[n-1] = a # たくさんキャッシュしたほが速い。
            #memo[n-2] = b
            #memo[n-3] = c
            local = a + b + c
            memo[n] = local
            #z = f(n-1) + f(n-2) + f(n-3); memo[n] = z # too slow
            return local
        return f(n)


samples = [
    4,
    25
]


for n in samples:
    ans = Solution().tribonacci(n)
    print(ans)