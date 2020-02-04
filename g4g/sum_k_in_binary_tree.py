#-*- coding: utf-8 -*-
"""

https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/
と
https://leetcode.com/problems/binary-tree-maximum-path-sum/
にてるし。
けど、inorderということが違うか。


"""

# Binary Tree Node
""" utility that allocates a newNode
with the given key """
class Node:
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def validate(path, k):
    #print("if sum of k in path; %s" % path)
    memo = []
    acc = 0
    for x in path:
        acc += x
        memo.append(acc)
    N = len(memo)
    #print("memo:%s, N:%s" % (memo, N))
    ans = set()
    for i in range(N):
        for j in range(N):
            # 0, 1, 2, 3, 4
            # 3, 2, 9, 7
            if i == j:
                subsum = memo[j]
            else:
                subsum = memo[j] - (memo[i-1] if i > 0 else 0)
            if subsum == k:
                #print("found: %s" % path[i:j+1])
                ans.add(str(path[i:j+1]))
    return ans

validate([1, -1, 4, 2], 5)
import sys
#sys.exit(0)
def preorder(node, k, path, gans):
    if node:
        path_copy = path[:]
        path_copy.append(node.data)
        preorder(node.left, k, path_copy, gans)
        preorder(node.right, k, path_copy, gans)

        #validate if there' k
        ans = validate(path_copy, k)
        gans.update(ans)

def printKPath(root, k):
    path = []
    gans = set()
    preorder(root, k, path, gans)
    for x in gans:
        print(x)

if __name__ == '__main__':

    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(6)

    k = 5
    printKPath(root, k)