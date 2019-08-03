#-*- coding: utf-8 -*-
from typing import List

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = self.leaves(root1)
        leaves2 = self.leaves(root2)
        #print("l1:%s and l2:%s" % (leaves1, leaves2))
        return leaves1 == leaves2

    def leaves(self, node):
        stack = []
        stack.append(node)
        leaves = []
        while len(stack) > 0:
            n = stack.pop()
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
            if n.right is None and n.left is None:
                leaves.append(n.val)
        return leaves

# root = TreeNode(5)
# sub = TreeNode(5)
# sub.right = TreeNode(-3)
# root.right = sub
#
# root1 = TreeNode(5)
# sub1 = TreeNode(-3)
# sub1.left = TreeNode(9)
# root1.left = sub1
#
# print(Solution().leafSimilar(root, root1))


root = TreeNode(5)
sub = TreeNode(3)
sub.right = TreeNode(-3)
root.right = sub

root1 = TreeNode(5)
sub1 = TreeNode(-3)
sub1.left = TreeNode(-3)
root1.left = sub1

print(Solution().leafSimilar(root, root1))
