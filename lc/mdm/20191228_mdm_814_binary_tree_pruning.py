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
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return self.__str__()

class Solution:
    """
    Remove subtree where not containing 1.
    In other word, remove subrtree only containing 0

    Approach.
    1. post-order, postdfs(node) -> bool
    def postdfs(node):
      node is None: tree
      if node.val is 0 and post(left) == true and post(right) == treu: treu
      return false

    O(N)

    Edge. what if node is None. return node.
    """
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        if root.val == 0 and not (root.left or root.right) : return None

        def dfs(node: TreeNode) -> bool:
            # True not containg a 1
            if node is None: return True
            a = dfs(node.left)
            b = dfs(node.right)

            if a: node.left = None
            if b: node.right = None
            if node.val == 0 and a and b:
                return True
            else:
                return False

        dfs(root)
        return root

#n = TreeNode(0)
n = TreeNode(1)
n1r = TreeNode(0)
n2l = TreeNode(0)
n2r = TreeNode(1)
n.right = n1r
n1r.left = n2l
n1r.right = n2r
ans = Solution().pruneTree(n)
def dfs(n):
    if n is None: return
    print("%s," % n.val, end=",")
    dfs(n.left)
    dfs(n.right)
dfs(ans)

