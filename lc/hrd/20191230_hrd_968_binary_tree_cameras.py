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

class Solution_my_botsu:
    def minCameraCover(self, root: TreeNode) -> int:
        cameras = [0]
        counter = [0]
        def is_camera_on_root_dfs(node: TreeNode, parent: TreeNode):
            if node is None: return None
            counter[0] += 1
            l = is_camera_on_root_dfs(node.left, node)
            r = is_camera_on_root_dfs(node.right, node)

            if l == False or r == False:
                cameras[0] += 1
                return True
            else:
                return False
        is_camera_on_root_dfs(root, None)
        return cameras[0] if counter[0] != 1 else 1

class Solution_greedy:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        #covered = {None}
        covered = set()
        covered.add(None)
        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if (par is None and node not in covered) or \
                    (node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})
        dfs(root)
        return self.ans

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def solve(node):
            if not node: return 0, 0 ,float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)
            return dp0, dp1, dp2
        dp = solve(root)
        return min(dp[1:])



# root = TreeNode(-10)
# root.left = TreeNode(9)
# n20 = TreeNode(20)
# n20.left = TreeNode(15)
# n20.right = TreeNode(7)
# root.right = n20
#root = TreeNode(-2)
#root.left = TreeNode(-1)
# root = TreeNode(-3)
# print("minCameraCover:%s" % Solution().minCameraCover(root))


# [0,0,null,null,0,0,null,null,0,0]

root = TreeNode(0)
n2 = TreeNode(0)
n3 = TreeNode(0)
n4 = TreeNode(0)
n5l = TreeNode(0)
n5r = TreeNode(0)
root.left = n2
n2.right = n3
n3.left = n4
n4.left = n5l
n4.right = n5r

print("minCameraCover:%s" % Solution().minCameraCover(root))




