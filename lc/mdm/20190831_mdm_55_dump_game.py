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
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 0: return False
        if length == 1: return True
        dp = [0] * length
        def dp_print():
            for row in dp:
                logging.debug(row)
        def dp_valid(i):
            if i < 0 or i >= length: return False
            else: return True
        def dp_get(i, default=0):
            if dp_valid(i): return dp[i]
            else: return default

        carryover_idx = 0
        for i in range(length):
            x = nums[i]
            possible_best_jumping_idx = i + x
            if dp[i] < i: return False
            carryover_idx = max(possible_best_jumping_idx, carryover_idx)
            if dp_valid(i+1):
                dp[i+1] = carryover_idx

        return True

class Solution_lte:
    @timeit
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 0: return False
        if length == 1: return True
        dp = [0] * length
        dp[0] = 1
        def dp_print():
            for row in dp:
                logging.debug(row)
        def dp_valid(i):
            if i < 0 or i >= length: return False
            else: return True
        def dp_get(i, default=0):
            if dp_valid(i): return dp[i]
            else: return default

        for i in range(length):
            if dp[i] > 0:
                for n in range(nums[i]):
                    if dp_valid(i+n+1):
                        dp[i+n+1] += 1

        return True if dp[i] > 0 else False



samples = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([0, 1], False),
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().canJump(S)
    assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))





