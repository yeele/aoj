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
    # O(n)
    def search_o_n(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def find_rotate_index(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return r

    def _search(self, nums, target):
        l, r = 0, len(nums)-1
        if l == r and nums[l] == target: return l
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if 0 <= r and r < len(nums) and nums[r] == target: return r
        return -1

    def search(self, nums: List[int], target: int) -> int:
        rotated_at = self.find_rotate_index(nums)
        found_at_1st_half = self._search(nums[:rotated_at], target)
        found_at_2nd_half = self._search(nums[rotated_at:], target)
        if found_at_1st_half != -1: return found_at_1st_half
        if found_at_2nd_half != -1: return rotated_at + found_at_2nd_half
        return -1

# 2224pm start
# 2240pm failed 159 / 196 test cases passed.
# 2244pm failed 168 / 196 test cases passed.
# 2246pm succeeded (22min, Great!)
samples = [
    # ([4,5,6,7,0,1,2], 0, 4),
    # ([4,5,6,7,0,1,2,], 3, -1),
    # ([1], 1, 0),
    ([1, 3], 3, 1),
]

for S, target, expected in samples:
    ans = Solution().search(S, target)
    print(ans)