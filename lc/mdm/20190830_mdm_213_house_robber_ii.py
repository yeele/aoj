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
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 0: return 0
        if length <= 3: return max(nums)

        # length >= 4
        dp = [0] * len(nums)
        def dp_get(i, default=0):
            if i < 0 or i >= length: return default
            else: return dp[i]

        # dp的にiまでの配列をつかった最大をほりこんでいけたと仮定(hypoth1)する
        # その上で漸化式をつくる
        # hypothXが可能か検討する yesなら実装 noならdp以外で再試行

        # Top included
        for i in range(length):
            dp[i] = max(dp_get(i-1), dp_get(i-2)+nums[i])
        maxi = dp[i-1]

        # Secound round without top
        dp[0] = 0 # bit of initializtion
        for i in range(1, length):
            dp[i] = max(dp_get(i-1), dp_get(i-2)+nums[i])
        return max(maxi, dp[i])



samples = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().rob(S)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))





