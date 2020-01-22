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
#https://leetcode.com/problems/find-eventual-safe-states/discuss/444740/classic-topological-sort-using-dfs
class Solution():
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        if N == 0: return []
        A = []
        visited = defaultdict(int)
        for i in range(N):
            if self.dfs(graph, i, visited):
                A.append(i)
        return A
    def dfs(self, graph, i, visited):
        if visited[i] == 2: return True
        if visited[i] == 1: return False
        visited[i] = 1
        for j in graph[i]:
            if self.dfs(graph, j, visited) == False: return False
        visited[i] = 2
        return True



S = [[1,2],[2,3],[5],[0],[5],[],[]]
#S = [[],[0,2,3,4],[3],[4],[]]
ans = Solution().eventualSafeNodes(S)
print(ans)
