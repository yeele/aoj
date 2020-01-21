#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
from typing import List
from collections import defaultdict
import sys

def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

from collections import defaultdict
import time

# let's improve Solution_working_but_LTE
class Solution_LTE():
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def is_cyclic(i):
            #       0     1    2   3   4   5  6
            # 0, [[1,2],[2,3],[5],[0],[5],[],[]]
            G = set(); B = set()
            def dfs(i):  # 1 -> 2 -> 5
                if i in memo: return memo[i]
                # G: [0, 1, 2]
                # B: [5]
                if i in G:
                    return True
                G.add(i)
                for next_i in graph[i]: # 1, 2 -> 2, 3
                    if next_i not in B:
                        if dfs(next_i): return True
                G.remove(i)
                B.add(i)
            ans = dfs(i)
            memo[i] = ans
            return ans == True

        A = []
        memo = {}
        for i in range(len(graph)):
            if not is_cyclic(i):
                A.append(i)
        return A

import collections
class Solution():
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        visisted = defaultdict(int) # 0, 1: visiting, 2: done
        def dfs(graph, i, visited):
            if visited[i] == 2: return True
            if visited[i] == 1: return False
            visited[i] = 1
            for j in graph[i]:
                if dfs(graph, j, visited) == False: return False
            visited[i] = 2
            return True
        A = []
        for i in range(N):  # O(N) number of nodes.
            if dfs(graph, i, visisted) == True: # in dfs O(E) , #edges
                A.append(i)
        return A





S = [[1,2],[2,3],[5],[0],[5],[],[]]
#S = [[],[0,2,3,4],[3],[4],[]]
ans = Solution().eventualSafeNodes(S)
print(ans)
