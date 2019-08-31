#Definition for singly-linked list.

def timeit(method):
    def timed(*args, **kw):
        global calc
        calc = defaultdict(int)
        print ('===========')
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.8f ms' % (method.__name__, (te - ts) * 1000))
        print("calc %s times" % sum(calc.values()))
        return result
    return timed


from typing import List
import sys
import logging
import itertools
from collections import defaultdict
import time

#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
class Solution:
    @timeit
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        def dp_print():
            for row in dp:
                logging.debug(row)
        def dp_valid(i, j):
            if i < 0 or i >= m: return False
            if j < 0 or j >= n: return False
            return True
        def dp_get(i, j, default=0):
            if dp_valid(i, j): return dp[i][j]
            else: return default
        # initialization
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
        # main process for dp filling
        for i in range(1, m):
            for j in range(1, n):
                if dp_valid(i-1, j):
                    dp[i][j] += dp_get(i-1, j)
                if dp_valid(i, j-1):
                    dp[i][j] += dp_get(i, j-1)


        dp_print()
        return dp[i][j]



samples = [
    (3, 2, 3),
    (7, 3, 28),
]
for m, n, expected in samples:
    print("-"*20)
    ans = Solution().uniquePaths(m, n)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (m, n, ans))





