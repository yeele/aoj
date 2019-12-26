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

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.order = []
    def rec(self, root) -> List[int]:
        if root is None: return
        self.order.append(root.val)
        for child_node in root.children:
            self.preorder(child_node)

    def preorder(self, root) -> List[int]:
        self.rec(root)
        return self.order


# follow up
# Recursive solution is trivial, could you do it iteratively?
    """
    あちゃー
    わからんかったわ。また。
    だからdiscussionみた。
    https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/454317/Python-recursive-and-iterative-solution-easy-to-understand
    """
class Solution:
    def preorder(self, root) -> List[int]:

        stack, order = [], []
        curr = root
        i = 0
        while curr or len(stack) > 0:
            i = 0
            if curr: #ポインタがあるとき
                # do something
                order.append(curr.val)
                stack.append((curr, i))
                if len(curr.children) > i:
                    curr = curr.children[i] # 左にすすめ
                else:
                    curr = None
                    i = 0
            else: #stackがあるので
                curr, i = stack.pop()
                i = i + 1 # I want do next one!
                # do something
                #curr = curr.right # 右にすすめ
                if len(curr.children) > i:
                    stack.append((curr, i))
                    curr = curr.children[i] # 左にすすめ
                else:
                    curr = None
                    i = 0

        return order













