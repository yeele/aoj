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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_recursive:
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        return self.ans
    def dfs(self, root: TreeNode) -> List[int]:
        if root is None: return
        self.dfs(root.left)
        #print(root.val)
        self.ans.append(root.val)
        self.dfs(root.right)
        return

class Solution_iterative_inorder:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, order = [], []
        curr = root
        while curr or len(stack) > 0:
            if curr:
                ##order.append(curr.val) # pre-order
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                order.append(curr.val) # inorder
                curr = curr.right
                ###order.append(curr.val) # postorder  ## No, post-order is bit more complicated
                ## see https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/459067/Tree's-3-orders-of-traversal-solutions-in-Python-easy-understand-with-comments
        return order

class Solution:
#class Solution_iterative_postorder:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, order = [], []
        curr = root
        while curr or len(stack) > 0:
            if curr:
                stack.append((curr, 1))
                curr = curr.left
            else:
                curr, visit = stack.pop()
                if visit == 2:
                    order.append(curr.val)
                    curr = None
                else:
                    stack.append((curr, 2))
                    curr = curr.right
        return order





root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.right = n1
n1.left = n2

ans = Solution().inorderTraversal(root)
print(ans)

