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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None: return 0
        maxi = [0] # 1
        def dfs(node: TreeNode):
            # return lengh of longest path in the subtree.
            if node is None: return 0
            a = dfs(node.left)
            b = dfs(node.right)
            local_maxi = 1 + max(a, b)
            maxi[0] = max(maxi[0],
                          (1 if a or b else 0) + (a if a else 0)+ (b if b else 0),
                          local_maxi
                          )
            return local_maxi
        dfs(root)
        return maxi[0] - 1 if maxi[0] >= 2 else 0

