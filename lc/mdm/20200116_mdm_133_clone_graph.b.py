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

# study from
# https://leetcode.com/problems/clone-graph/discuss/478738/Intuitive-Python-BFS
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        from collections import deque
        if node is None: return None
        q = deque()
        visited = {}
        visited[node] = Node(node.val) # 最初に作っておく
        q.append(node)
        """
        queueに入れる前に具現がされていること！
        """
        while len(q) > 0:
            curr: Node = q.popleft()  # q = [4], cloned = {1: 1', 2: 2', 4: 4'}
            for neighbor in curr.neighbors: # q = [4], curr = 2
                if neighbor not in visited: # neighbors = [1, 3]
                    visited[neighbor] = Node(neighbor.val) # cloned = {1: 1', 2: 2', 4: 4', 3:3'}
                    q.append(neighbor) # q = [2, 4]
                # visited[1] = 1' -> neighors(2', 4')
                # visited[2] = 2' -> neighors(1')
                visited[curr].neighbors.append(visited[neighbor]) # すでに具現化されているので。

        return visited[node]







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