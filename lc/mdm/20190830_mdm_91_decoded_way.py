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
    """
    1.  O(2^(n/2)) => O(2^n) = １文字とるパターンと２文字とるパターンでの再帰
    2.

    """
    @timeit
    def numDecodings(self, s: str) -> int:
        # non-empyt is guranteeed by the problem description
        length = len(s)
        dp = [0] * length
        dp[0] = 1
        if len(s) == 1 and s == "0": return 0
        if len(s) == 1: return 1
        if len(s) == 2: return 2
        dp[1] = 2

        # assuming that all the input are sanitized
        def dp_print():
            for row in dp:
                logging.debug(row)
        def dp_get(i, default=0):
            if i < 0 or i >= length: return default
            return dp[i]

        for i in range(2, length):
            if int(s[i-1] + s[i]) <= 26:
                dp[i] = dp_get(i-2) + dp_get(i-1)
            else:
                dp[i] = dp_get(i-1)
        dp_print()
        return dp[i]




samples = [
    ("12", 2),
    ("226", 3),
    ("2262", 3),
    ("2212", 5),
    ("0", 0)
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().numDecodings(S)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))





