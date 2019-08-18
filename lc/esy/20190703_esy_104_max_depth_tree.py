#-*- coding: utf-8 -*-
from typing import List

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def p(self):
        print("%s" % self.val)
        if self.left: self.left.p()
        if self.right: self.right.p()

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        else: return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
            )

    def printAll(self, root: TreeNode):
        root.p()


root = TreeNode(3)
root.left = TreeNode(9)
n20 = TreeNode(20)
n20.left = TreeNode(15)
n20.right = TreeNode(7)
root.right = n20

Solution().printAll(root)
print(Solution().maxDepth(root))

root = TreeNode(1)
root.left = None
root.right = TreeNode(2)

Solution().printAll(root)
print("maxDepth:%s" % Solution().maxDepth(root))
