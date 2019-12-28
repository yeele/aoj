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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def is_same(a, b):
            if a is None and b is None: return True
            if a.val != b.val: return False
            if is_same(a.left, b.left) and is_same(a.right, b.right):
                return True
            else:
                return False

        return is_same(p, q)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.left = n3

n1a = TreeNode(1)
n2a = TreeNode(2)
n3a = TreeNode(3)
n1a.left = n2a
n1a.left = n3a


ans = Solution().isSameTree(n1, n1a)
print(ans)


