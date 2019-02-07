#-*- coding: utf-8 -*-
"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visit = root.val
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

