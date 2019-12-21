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
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def node2str(node: TreeNode, d=0):
    if node != None:
        return("l{}#{}#r{}".format(
            node2str(node.left),
            node.val,
            node2str(node.right),
        ))
    else:
        return ''

class Solution_me1st:
    @timeit
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        memo = defaultdict(list)
        def dfs(node):
            memo[node2str(node)].append(node)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        ans = []
        for node_label, candidate in memo.items():
            if len(candidate) >=2:
                # 1個でいいらしい。
                ans.append(candidate.pop())
        return ans

#https://leetcode.com/problems/find-duplicate-subtrees/discuss/416674/Python-dfs-path-map-to-node
class Solution_lc:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res=[]
        m=defaultdict(set)
        # (path, root node), use 'l' and 'r' to differentiate same-value-but-different-structure sub trees.
        def dfs(node):
            if not node:return ''
            left=dfs(node.left)
            right=dfs(node.right)
            print(left,right,node.val)
            m[left+str(node.val)+right].add(node)
            return left+'l'+str(node.val)+right+'r'
        dfs(root)
        for path in m:
            print("path:%s -> %s" % (path, m[path]))
            if len(m[path])>1:
                res.append(m[path].pop())
        return res

class Solution: #2nd
    @timeit
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        memo = defaultdict(list)
        def dfs(node):
            if not node: return ''
            left = dfs(node.left)
            right = dfs(node.right)
            key = left + 'l' + str(node.val) + right + 'r'
            print("key -> {}".format(key))
            memo[key].append(node)
            return key
        dfs(root)
        ans = []
        for node_label, candidate in memo.items():
            print("node_label:%s -> %s" % (node_label, memo[node_label]))
            if len(candidate) >=2:
                # 1個でいいらしい。
                ans.append(candidate.pop())
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)


# print("4 = %s" % (node2str(root.left.left)))
# print("2->4 = %s" % (node2str(root.left)))
ans = Solution().findDuplicateSubtrees(root)
print(ans)
