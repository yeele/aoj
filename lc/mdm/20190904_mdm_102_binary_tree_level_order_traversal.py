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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # とりあえずstack にrootいれて、
        # stackから全部とりだして、全部露出して
        # そしてサブ木はまた全部stackにプッシュする。くりかえし。
        # これでいけそう。O(n)
        # いちおう、再帰的なかんがえかたもしておこう。
        # bfsって再帰的にできるの？やるとしたらlevelの記憶とglobal 変数へ値格納、そんなところか。
        # では。
        # 最初の説明、それはbfsそのものだと思うが、それを実装する。

        if root == None: return []
        stack = [root]
        ans = []
        while len(stack) > 0:
            another_stack = []
            leveled_nodes = []
            while len(stack) > 0:
                node = stack.pop(0)
                if node != None:
                    leveled_nodes.append(node.val)
                if node.left: another_stack.append(node.left)
                if node.right: another_stack.append(node.right)
            ans.append(leveled_nodes)
            stack.extend(another_stack)
        return ans

samples = [
    (
        [
            [1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0],
        ], 1
    ),
    (
        [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1],
        ],
        3
    )
]

for S, expected in samples:
    print("-"*20)
    S = [list(map(lambda x: str(x), row)) for row in S]
    ans = Solution().numIslands(S)
    assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))
