#-*- coding: utf-8 -*-
from typing import List

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def p(self):
        print("%s" % self.val)
        if self.left: self.left.p()
        if self.right: self.right.p()

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #print("p:%s and q:%s" % (p, q))
        if q is None and p is None: return True
        if p is None and q: return False
        if q is None and p: return False
        if p.val == q.val:
            if p.left is None and q.left is None and p.right is None and q.right is None:
                return True
            else:
                return self.isSameTree(p.left, q.left) and \
                       self.isSameTree(p.right, q.right)
        else: return False


    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        else: return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
            )

    def printAll(self, root: TreeNode):
        root.p()


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
#
# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.right = TreeNode(3)
#
# Solution().printAll(root)
# print(Solution().isSameTree(root, root1))
#
#
# root = TreeNode(1)
# root.left = TreeNode(2)
#
# root1 = TreeNode(1)
# root1.right = TreeNode(3)
#
# Solution().printAll(root)
# print(Solution().isSameTree(root, root1))
#
#
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
#
# root1 = TreeNode(1)
# root1.left = TreeNode(3)
# root1.right = TreeNode(2)
#
# Solution().printAll(root)
# print(Solution().isSameTree(root, root1))



# root = TreeNode(1)
#
# root1 = None
#
# Solution().printAll(root)
# print(Solution().isSameTree(root, root1))

# [5,null,5,null,-3]
# [5,-3,null,9]

root = TreeNode(5)
sub = TreeNode(5)
sub.right = TreeNode(-3)
root.right = sub

root1 = TreeNode(5)
sub1 = TreeNode(-3)
sub1.left = TreeNode(9)
root1.left = sub1

Solution().printAll(root)
print(Solution().isSameTree(root, root1))
