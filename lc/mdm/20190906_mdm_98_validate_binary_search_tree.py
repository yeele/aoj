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



class Solution:
    def isValidBST(self, root: TreeNode, parent=None) -> bool:

        if root is None: return True

        if root.left:
            if root.val > root.left.val and self.isValidBST(root.left, root.val):
                if parent:
                    if root.left.val > parent:
                        pass # ok
                    else:
                        return False
            else:
                return False
        if root.right:
            if root.val < root.right.val and self.isValidBST(root.right, root.val):
                if parent:
                    if root.right.val < parent:
                        pass # ok
                    else:
                        return False
            else:
                return False

        return True


root = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(3)
root.left = n1
root.right = n2

ans = Solution().isValidBST(root)
logging.debug("%s" % ans)


"""
    5
   / \
  1   4
     / \
    3   6
"""
root = TreeNode(5)
n1 = TreeNode(1)
n2 = TreeNode(4)
root.left = n1
root.right = n2
n3 = TreeNode(3)
n4 = TreeNode(6)
n2.left = n3
n2.right = n4


ans = Solution().isValidBST(root)
logging.debug("%s" % ans)


"""
[10,5,15,null,null,6,20]
"""

root = TreeNode(10)
n1 = TreeNode(5)
n2 = TreeNode(15)
root.left = n1
root.right = n2
n3 = TreeNode(6)
n4 = TreeNode(20)
n2.left = n3
n2.right = n4

ans = Solution().isValidBST(root)
logging.debug("%s" % ans)


"""
[3,1,5,0,2,4,6]
一応、進んでいる、テストケースは進んでは、さらに進んだケースで
止まっているだけなので、報告性はよしとしよう

"""
root = TreeNode(3)
n1 = TreeNode(1)
n2 = TreeNode(5)
root.left = n1
root.right = n2
n3 = TreeNode(0)
n4 = TreeNode(2)
n1.left = n3
n1.right = n4
n5 = TreeNode(4)
n6 = TreeNode(6)
n2.left = n5
n2.right = n6

ans = Solution().isValidBST(root)
logging.debug("%s" % ans)

