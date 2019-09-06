#Definition for singly-linked list.

def timeit(method):
    def timed(*args, **kw):
        global calc
        calc = defaultdict(int)
        print ('===========')
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.8f ms' % (method.__name__, (te - ts) * 1000))
        print("calc %s times" % sum(calc.values()))
        return result
    return timed


from typing import List
import sys
import logging
import itertools
from collections import defaultdict
import time
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_not_enough_idea:
    def rec_lefty(self, i, j, P: List[int], I: List[int]) -> TreeNode:
        if i >= len(P): return None
        if j <= i: return None # invalid i, j relation
        value = P[i]
        node = TreeNode(value)
        node.left = self.rec_lefty(i+1, j, P, I)
        return node

    def rec(self, i, j, P: List[int], I: List[int]) -> TreeNode:
        # i start, j is end(exclusive)
        if i >= len(P): return None
        if j <= i: return None # invalid i, j relation

        value = P[i]
        node = TreeNode(value)
        # find
        for k in range(i, j):
            if I[k] == value: break

        if k < j: #　見つかった
            node.left = self.rec_lefty(i+1, k+1, P, I)
            node.right = self.rec(k+1, j, P, I)
        else: # 見つかってない
            #node.left = self.rec(i+1, j, P, I)
            node.left = self.rec_lefty(i+1, j, P, I)
        return node


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.rec(0, len(preorder), preorder, inorder)




class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder is None or inorder is None: return None
        if len(preorder) == 0 or len(inorder) == 0: return None
        node = TreeNode(preorder.pop(0))
        rootIdx = inorder.index(node.val)
        inorder_left  = inorder[:rootIdx]
        inorder_right = inorder[rootIdx+1:]
        node.left = self.buildTree(preorder, inorder_left)
        node.right = self.buildTree(preorder, inorder_right)
        return node



def bfs_print(node: TreeNode):
    stack = [node]
    while len(stack) > 0:
        n = stack.pop(0)
        logging.debug("null" if n is None else n.val)
        if n:
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)
    return


# samples = [
#     #([3,9,20,15,7], [9,3,15,20,7]),
#     ([1, 2, 3], [3, 2, 1]),
#     ([1, 2, 3], [2, 3, 1]),
# ]
#
# for preorder, inorder in samples:
#     ans = Solution().buildTree(preorder, inorder)
#     bfs_print(ans)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)


n1.right = n2
n2.right = n3
#n3.left = n4
n3.right = n4
n4.right = n5


def print_inorder(node: TreeNode):
    if node:
        print_inorder(node.left)
        print(node.val, end=",")
        print_inorder(node.right)

def print_preorder(node: TreeNode):
    if node:
        print(node.val, end=",")
        print_preorder(node.left)
        print_preorder(node.right)

print('------------- preorder -----------')
print_preorder(n1)
print()

print('------------- inorder -----------')
print_inorder(n1)
print()