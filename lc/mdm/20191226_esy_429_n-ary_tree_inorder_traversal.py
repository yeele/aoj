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
    def __str__(self):
        return "%s" % self.val
    def __repr__(self):
        return self.__str__()

class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        if root is None: return [[]]
        stack = [root]
        ans = [root.val]
        while len(stack) > 0:
            # do making each layer as an array
            node = stack.pop()
            layer = [child.val for child in node.children]
            ans.append(layer)
        return ans
        """
        if root is None: return []
        stack = [root]
        ans = []  # [1, ]
        while len(stack) > 0:
            layer_ans = []
            layer_stack = []
            for node in stack:
                # do making each layer as an array
                layer_ans.append(node.val)
                if node.children is None: continue
                for child in node.children:
                    layer_stack.append( child )
            ans.append(layer_ans)
            stack = layer_stack
        return ans


# I like someone thinking recursive solution
# which I think it's harder

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/341223/Python-DFS-solution


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
#
# n1.children = [n3, n2, n4]
# n3.children = [n5, n6]

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)
n14 = Node(14)

n1.children = [n2, n3, n4, n5]
n3.children = [n6, n7]
n7.children = [n11]
n11.children = [n14]
n4.children = [n8]
n5.children = [n9, n10]
n8.children = [n12]
n9.children = [n13]

ans = Solution().levelOrder(n1)
print(ans)


