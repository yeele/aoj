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

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    def rec(self, node: Node, cloned):
        if node is None: return None
        if node.val not in cloned:
            new_node = Node(node.val) # let's clone
            cloned[node.val] = new_node
            for next_node in node.neighbors:
                self.rec(next_node, cloned)

    def rec2(self, node: Node, cloned, visited):
        if node is None: return None
        if node.val not in visited or visited[node.val] == 0:
            new_node = cloned[node.val]
            # neighbors creation
            for next_node in node.neighbors:
                new_node.neighbors.append(cloned[next_node.val])
            visited[node.val] = 1
            for next_node in node.neighbors:
                self.rec2(next_node, cloned, visited)


    def cloneGraph(self, node: Node) -> Node:
        if node is None: return None
        cloned = {}
        self.rec(node, cloned)
        visited = {}
        self.rec2(node, cloned, visited)
        return cloned[node.val]







# adjList = [[2,4],[1,3],[2,4],[1,3]]
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]


ans = Solution().cloneGraph(n1)
print(ans)