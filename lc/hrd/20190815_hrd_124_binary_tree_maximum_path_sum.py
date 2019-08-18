#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""
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
    def printAll(self, root: TreeNode):
        root.p()
    def __init__(self):
        self.maxi = -sys.maxsize - 1


    def rec(self, node: TreeNode) -> int:
        if node == None: return -sys.maxsize - 1
        max_left = self.rec(node.left)
        max_right = self.rec(node.right)
        x = max(
            node.val,
            max_left, max_right,
            max_left + node.val, max_right + node.val)
        # print("current max is %s" % x)
        # print("max_left %s, max_right %s, node.val %s" % (max_left, max_right, node.val))
        self.maxi = max(self.maxi, x, max_left + max_right + node.val)
        if node.val < 0:
            return max(max_left + node.val, max_right + node.val)
        else:
            return x

    def maxPathSum(self, node: TreeNode) -> int:
        self.maxi = -sys.maxsize - 1
        self.rec(node)
        return self.maxi

root = TreeNode(-10)
root.left = TreeNode(9)
n20 = TreeNode(20)
n20.left = TreeNode(15)
n20.right = TreeNode(7)
root.right = n20

Solution().printAll(root)
print("maxPathSums:%s" % Solution().maxPathSum(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
Solution().printAll(root)
print("maxPathSum:%s" % Solution().maxPathSum(root))


root = TreeNode(-3)
Solution().printAll(root)
print("maxPathSum:%s" % Solution().maxPathSum(root))

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

root = stringToTreeNode("[1,-2,-3,1,3,-2,null,-1]")
Solution().printAll(root)
print("maxDepth:%s" % Solution().maxPathSum(root))

root = stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
Solution().printAll(root)
print("maxDepth:%s" % Solution().maxPathSum(root))

