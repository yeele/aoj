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



class Solution_mine:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        stack, order = [root], []
        while len(stack) > 0:
            layer_stack = []
            layer_order = []
            for node in stack:
                layer_order.append(node.val)
                if node.left: layer_stack.append(node.left)
                if node.right: layer_stack.append(node.right)

            #order.append(layer_order)
            order.insert(0, layer_order)
            stack = layer_stack
        return order

# optimal solution Not using insert since insert is O(N)
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs%2Bstack-bfs%2Bqueue).
# His idea is to put slice in the end. Slice take O(a-b) may take O(N) as worst, hoever,
# this is outside of scope :) so overall O is O(N). smart :)
class Solution:
    def levelOrderBottom(self, root):
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [
                child for node in queue if node
                for child in (node.left, node.right)
            ]
        return res[-2::-1]


n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)
n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7

ans = Solution().levelOrderBottom(n3)
print(ans)


