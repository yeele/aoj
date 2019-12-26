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

class Solution_rec:
    def __init__(self):
        self.order = []
    def postorder(self, root) -> List[int]:
        """
        postっていうのは root-last order
        なので
        1
        2 3
        とうツリーの場合は2 -> 3 -> という順番でございます。
        """
        def rec(root):
            if root is None: return
            for child in root.children:
                rec(child)
            self.order.append(root.val)
        rec(root)
        return self.order

from collections import namedtuple
Track = namedtuple('Track', ['node', 'visisted'])
class Solution:
    def postorder(self, root) -> List[int]:
        if root is None: return []
        stack, order = [Track(root, 1)], []
        curr = root
        while curr or len(stack) > 0:
            if curr:
                if curr.children and len(curr.children) > 0:
                    for i in range(len(curr.children)-1, -1, -1):
                        node = curr.children[i]
                        if i == 0:
                            stack.append(Track(node, 1))
                        else:
                            stack.append(Track(node, 0))
                    curr = curr.children[0]
                else:
                    curr = None
            else:
                track = stack.pop()
                curr, visited = track.node, track.visisted
                if curr.children is None or len(curr.children) == 0 or visited == 1:
                    order.append(curr.val)
                    curr = None
                else:
                    stack.append(Track(curr, 1))
        return order

# does this work??
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/440303/Python-3-Iterative-Faster-than-91.14-100-better-memorywise
class Solution_lc:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        self.list = []
        while stack:
            node = stack.pop()
            self.list.append(node.val)
            if node.children:
                for i in node.children:
                    stack.append(i)
        print(self.list)
        return self.list[::-1]

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/460888/Simple-Iterative-Python-Solutiono
# こいつをpostorderに改造する
class Solution:
    def __preorder(self, root):
        stack = [root]; res = []
        while len(stack) > 0:
            current = stack.pop()
            res.append(current.val)
            if current.children:
                for node in current.children[::-1]:
                    stack.append(node)
        return res

    def __inorder(self, root):
        stack = [root]; res = []
        while len(stack) > 0:
            current = stack.pop(0)
            res.append(current.val)
            if current.children:
                for node in current.children:
                    stack.append(node)
        return res

    """
    thanks I finally understand it by looking this solution.
    https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/432121/Python-Intuitive-Iterative-Solution-One-Stack
    """
    def __postorder(self, root):
        stack = [root]; res = []
        while len(stack) > 0:
            current = stack.pop()
            res.insert(0, current.val)
            if current.children:
                for node in current.children:
                    stack.append(node)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        print("preorder: %s" % self.__preorder(root))
        print("inorder: %s" % self.__inorder(root))
        print("postorder: %s" % self.__postorder(root))

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

ans = Solution().postorder(n1)
print(ans)


