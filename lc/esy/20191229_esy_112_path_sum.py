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

class Solution:
    """
    edge case: (initial acc is 0 , what if sum = 0 is given?!)
      root = [1], sum = 0
    edge case: ( return True only if it reaches to the end of branch)
      https://leetcode.com/submissions/detail/289318789/
      root = [1, 2], sum = 1
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # dfsでaccumulative sumをcarry on すればよい
        def dfs_accumulate(node, goal: int, acc:int,) -> bool:
            if node is None: return False
            _acc = 0 if acc == None else acc
            _acc_new = _acc + node.val
            is_leaf = (node.left == None and node.right == None)
            if _acc_new == goal and is_leaf:
                return True
            if node.left:
                if dfs_accumulate(node.left, goal, _acc_new): return True
            if node.right:
                if dfs_accumulate(node.right, goal, _acc_new): return True
            return False

        if root is None: return False

        return dfs_accumulate(root, sum, None)


