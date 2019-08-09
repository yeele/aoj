#-*- coding: utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math
class Solution:
    def rec(self, nums: List[int]) -> TreeNode:
        if nums == None or len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            bigger = TreeNode(nums[1])
            smaller = TreeNode(nums[0])
            bigger.left = smaller
            return bigger
        elif len(nums) == 3:
            bigger = TreeNode(nums[2])
            mid = TreeNode(nums[1])
            smaller = TreeNode(nums[0])
            mid.left = smaller
            mid.right = bigger
            return mid
        else:
            mid = math.floor(len(nums)/2)
            root = TreeNode(nums[mid])
            root.left = self.rec(nums[:mid])
            root.right = self.rec(nums[mid+1:])
            return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # what if nums is null or empty
        return self.rec(nums)

def dfs(node: TreeNode):
    if node is not None:
        print (node.val)
        dfs(node.left)
        dfs(node.right)

samples = [
    [-10,-3,0,5,9],
]
for sample in samples:
    ans = Solution().sortedArrayToBST(sample)
    dfs(ans)


