#-*- coding: utf-8 -*-
"""
https://leetcode.com/problems/two-sum/description/
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hope = {}
        for i, x in enumerate(nums):
            if x in hope.keys():
                return [hope[x], i]
            hope[target - x] = i





"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
nums = [2, 7, 11, 15]
target = 9
foo = Solution()
print (foo.twoSum(nums, target))