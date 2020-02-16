#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
from typing import List
from collections import defaultdict
import sys

def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

from collections import defaultdict
import time


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [1, 2, 3]
        def rec(nums, chosen):
            #print("chose:%s" % chosen)
            if len(nums) == 0:
                return [chosen[:]]
            N = len(nums)
            A = []
            for i in range(N):
                T = nums[i]
                chosen.append(T)
                nums.remove(T)
                B = rec(nums, chosen)
                if len(B) > 0:
                    A += B
                chosen.remove(T)
                nums.insert(i, T)
            return A

        return rec(nums, [])




samples = [
    (
        [1, 2, 3]
    )


]
for S in samples:
    ans = Solution().permute(S)
    print(ans)
