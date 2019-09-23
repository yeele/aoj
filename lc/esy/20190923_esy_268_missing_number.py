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
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)+1):
            total += i
        return total - sum(nums)



class Solution_space:
    def missingNumber(self, nums: List[int]) -> int:
        memo = [0] * (len(nums)+1)
        for i, n in enumerate(nums):
            memo[n] = 1
        print(memo)
        for i, n in enumerate(memo):
            if memo[i] == 0:
                return i
        return None


samples = [
    ([3,0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),

]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for S, expected in samples:
    ans = Solution().missingNumber(S)
    print(ans)
