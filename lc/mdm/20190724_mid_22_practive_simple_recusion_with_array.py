#-*- coding: utf-8 -*-
from typing import List

#Definition for a binary tree node.
"""
Title: tech blog recursive で　リストを返す。

Treeがあって末端の深さのリストを返す問題
例えば

      3
     / \
    4    9
   / \       
  8  10

という木があったら

[3, 3, 2]というツリーを返す問題。

を解いてみよう。
なぜなら、22の括弧問題で、一向に正解のリストが返せなかったらからである"""
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
    def maxDepth(self, root: TreeNode, depth=0) -> int:
        if root == None:
            return [depth]
        else:
            rets = []
            left_depth = self.maxDepth(root.left, depth+1)
            right_depth = self.maxDepth(root.right, depth+1)
            rets += left_depth
            rets += right_depth
            rets = list(set(rets))
            return rets


    def printAll(self, root: TreeNode):
        root.p()


root = TreeNode(3)
root.left = TreeNode(9)
n20 = TreeNode(20)
n20.left = TreeNode(15)
n20.right = TreeNode(7)
root.right = n20

#Solution().printAll(root)
print(Solution().maxDepth(root))

root = TreeNode(1)
root.left = None
root.right = TreeNode(2)

#Solution().printAll(root)

print("maxDepth:%s" % Solution().maxDepth(root))