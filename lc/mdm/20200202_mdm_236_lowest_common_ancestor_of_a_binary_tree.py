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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q:TreeNode) -> TreeNode:
        lca = [None]
        def dfs(node, p, q):
            # looking for p OR q
            if node:
                ret_m = node.val == p.val or node.val == q.val
                ret_l = dfs(node.left, p, q)
                ret_r = dfs(node.right, p, q)
                if (ret_l and ret_r) or (ret_m and ret_l) or (ret_m and ret_r):
                    if lca[0] is None:
                        lca[0] = node
                    return True
                return any([ret_m, ret_l, ret_r])
            return False
        ans = dfs(root, p, q)
        return lca[0] if lca[0] else root


t3 = TreeNode(3)
t5 = TreeNode(5)
t1 = TreeNode(1)
t6 = TreeNode(6)
t2 = TreeNode(2)
t7 = TreeNode(7)
t4 = TreeNode(4)
t0 = TreeNode(0)
t8 = TreeNode(8)

t3.left = t5
t3.right = t1
t5.left = t6
t5.right = t2
t2.left = t7
t2.right = t4
t1.left = t0
t1.right = t8

print(Solution().lowestCommonAncestor(t3, t5, t1))
print(Solution().lowestCommonAncestor(t3, t4, t6))
print(Solution().lowestCommonAncestor(t3, t2, t8))
print(Solution().lowestCommonAncestor(t3, t0, t8))
print(Solution().lowestCommonAncestor(t3, t0, t1))