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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def is_same_tree(a: TreeNode, b: TreeNode):
            if a == None and b == None: return True
            if a is None and b: return False
            if b is None and a: return False
            if a.val == b.val:
                return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)
            else:
                return False

        def dfs(node: TreeNode):
            if is_same_tree(node, t):
                return True
            if node.left:
                if dfs(node.left): return True
            if node.right:
                if dfs(node.right): return True
            return False

        return dfs(s)



