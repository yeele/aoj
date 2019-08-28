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

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 0: return 0

        dp = [0] * len(nums)
        def dp_get(i, default=0):
            if i < 0 or i >= length: return default
            else: return dp[i]

        # dp的にiまでの配列をつかった最大をほりこんでいけたと仮定(hypoth1)する
        # その上で漸化式をつくる
        # hypothXが可能か検討する yesなら実装 noならdp以外で再試行

        for i in range(length):
            dp[i] = max(dp_get(i-1), dp_get(i-2)+nums[i])
        return dp[i]



