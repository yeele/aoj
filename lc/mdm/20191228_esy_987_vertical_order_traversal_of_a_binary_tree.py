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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        res = defaultdict(lambda : defaultdict(list))

        def dfs(node: TreeNode, x: int, y: int, res):
            if node is None: return
            _y = abs(y)
            res[x][_y].append(node.val) # _y is abs y is guarateed that 1 direction
            dfs(node.left, x - 1, y - 1, res)
            dfs(node.right, x + 1, y - 1, res)

        dfs(root, 0, 0, res)
        # cost of sorted(dict.iteritems())??
        ans = []
        for x, xaxis in sorted(res.items()):
            v_res = []
            for y, vertical_ary in sorted(xaxis.items()):
                v_res += sorted(vertical_ary)
            ans.append(v_res)
        return ans

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)
n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7

ans = Solution().verticalTraversal(n3)
print(ans)

n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n0.right = n1
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

ans = Solution().verticalTraversal(n0)
print(ans)








class Solution_botsu:
    """
    複雑過ぎて、デバッグできなかったコード。
    """
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        res0, resM, resP = [], [], []

        def dfs(node: TreeNode, x: int, y: int, res0, resM, resP):
            if node is None: return
            # do something with node.val
            if x == 0: # I don't have to generate
                if len(res0) == 0:
                    res0.append([node.val])
                else:
                    res0[0].append(node.val)
            elif x < 0:
                if len(resM) < abs(x):
                    resM.append([node.val])
                else:
                    resM[abs(x)-1].append(node.val)
            else: # x > 0
                if len(resP) < abs(x):
                    resP.append([node.val])
                else:
                    resP[abs(x)-1].append(node.val)
            dfs(node.left, x - 1, y - 1, res0, resM, resP)
            dfs(node.right, x + 1, y - 1, res0, resM, resP)

        dfs(root, 0, 0, res0, resM, resP)
        res = []
        for vertical in reversed(resM):
            res.append(vertical)
        for vertical in res0:
            res.append(vertical)
        for vertical in resP:
            res.append(vertical)

        return res