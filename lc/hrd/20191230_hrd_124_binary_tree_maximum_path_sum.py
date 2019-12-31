#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        if root is None: return 0
        maxi = [root.val]
        def dfs(node: TreeNode):
            if node is None: return None
            max_l = dfs(node.left)
            max_r = dfs(node.right)
            candidate = []
            if max_l is not None: candidate.append(max_l)
            if max_r is not None: candidate.append(max_r)

            local = max(
                node.val,
                node.val + (max(candidate) if len(candidate) > 0 else 0)
            )
            maxi[0] = max(maxi[0],
                          local,
                          node.val + (sum(candidate) if len(candidate) > 0 else 0),
                          max(candidate) if len(candidate) > 0 else node.val
                          )
            return local
        dfs(root)
        return maxi[0]

# root = TreeNode(-10)
# root.left = TreeNode(9)
# n20 = TreeNode(20)
# n20.left = TreeNode(15)
# n20.right = TreeNode(7)
# root.right = n20
#root = TreeNode(-2)
#root.left = TreeNode(-1)
root = TreeNode(-3)
print("maxPathSums:%s" % Solution().maxPathSum(root))


