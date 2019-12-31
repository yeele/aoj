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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://leetcode.com/problems/path-sum-ii/discuss/464828/Java-solution-100-Recursive
# この回答をみて、あー、これがすんなりできるようになりたい。と
# 沿う感じたのでさる。


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def rec(node: TreeNode, goal, acc, path):
            if node is None: return
            path.append(node.val)
            _acc = (acc if acc else 0) + node.val
            if _acc == goal and node.left is None and node.right is None:
                copied = path[:]
                res.append(copied)
            rec(node.left, goal, _acc, path)
            rec(node.right, goal, _acc, path)
            # revert
            path.pop()
        rec(root, sum, None, [])
        return res


class Solution_ok_but_heavy_memory:
    """
    edge case: (initial acc is 0 , what if sum = 0 is given?!)
      root = [1], sum = 0
    edge case: ( return True only if it reaches to the end of branch)
      https://leetcode.com/submissions/detail/289318789/
      root = [1, 2], sum = 1
    """
    def __init__(self):
        self.values = []

    def pathSum(self, root: TreeNode, sum: int) -> bool:
        # dfsでaccumulative sumをcarry on すればよい
        def dfs_accumulate(node, goal: int, acc:int, values: List[int]) -> bool:
            if node is None: return
            _acc = 0 if acc == None else acc
            _acc_new = _acc + node.val
            values.append(node.val)
            copied_values_left = values[:]
            copied_values_right = values[:]
            is_leaf = (node.left == None and node.right == None)
            if _acc_new == goal and is_leaf:
                self.values.append(copied_values_left)
            if node.left:
                dfs_accumulate(node.left, goal, _acc_new, copied_values_left)
            if node.right:
                dfs_accumulate(node.right, goal, _acc_new, copied_values_right)

        if root is None: return []

        dfs_accumulate(root, sum, None, [])
        return self.values


n5 = TreeNode(5)
n4 = TreeNode(4)
n8 = TreeNode(8)
n11 = TreeNode(11)
n13 = TreeNode(13)
n4b = TreeNode(4)
n7 = TreeNode(7)
n2 = TreeNode(2)
n5b = TreeNode(5)
n1 = TreeNode(1)

n5.left = n4
n5.right = n8
n4.left = n11
n11.left = n7
n11.right = n2
n8.left = n13
n8.right = n4b
n4b.left = n5b
n4b.right = n1

ans = Solution().pathSum(n5, 22)
print(ans)