#-*- coding: utf-8 -*-
from typing import List

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print(self, depth=0):
        print("%s%s" % ('  '*depth, self.val))
        if self.left: self.left.print(depth+1)
        if self.right: self.right.print(depth+1)

class Solution:
    def rec(self, node: TreeNode):
        if node is None: return None
        tmp = node.left
        node.left = node.right
        node.right = tmp
        if node.left is not None: self.invertTree(node.left)
        if node.right is not None: self.invertTree(node.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.rec(root)
        return root




node = TreeNode(4)
sub = TreeNode(2)
sub.left = TreeNode(1)
sub.right = TreeNode(3)
node.left= sub
r1 = TreeNode(7)
r1.left = TreeNode(6)
r1.right = TreeNode(9)
node.right= r1

node.print()
Solution().invertTree(node).print()


node.print()
Solution().invertTree(None)
