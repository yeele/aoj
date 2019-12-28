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



class Solution_iterative:
    def validate(self, layer: List[int]):
        #print("layer:%s" % layer)
        if layer is None or len(layer) == 0: True
        l = 0
        r = len(layer) - 1
        while l <= r:
            #print("layer[l]:%s != layer[r]:%s" % (layer[l], layer[r]))
            if layer[l] != layer[r]: return False
            l += 1
            r -= 1
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True

        stack = [root]
        while len(stack) > 0:
            layer_stack = []
            layer = [n.val if n else 'null' for n in stack]
            # validate layer
            if not self.validate(layer): return False
            for n in stack:
                if n:
                    layer_stack += [n.left, n.right]
            stack = layer_stack
        return True



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def rec(node1, node2):
            if node1 is None and node2 is None: return True
            if node1 is None and node2: return False
            if node1 and node2 is None: return False
            # どっちもノード有り
            if node1.val != node2.val: return False
            # ここは味噌。n1の左と右を比較している訳ではないことに注意!
            return rec(node1.left, node2.right) and rec(node1.right, node2.left)

        if root is None: return True
        return rec(root.left, root.right)




n1 = TreeNode(1)
n2a = TreeNode(2)
n2b = TreeNode(2)
n3a = TreeNode(3)
n3b = TreeNode(3)
n4a = TreeNode(4)
n4b = TreeNode(4)

n1.left = n2a
n1.right = n2b
n2a.left = n3a
n2a.right = n4a
n2b.left = n4b
n2b.right = n3b

ans = Solution().isSymmetric(n1)
print(ans)


