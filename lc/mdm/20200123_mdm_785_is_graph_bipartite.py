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

class unionfind:
    def __init__(self, n):
        self.n = n
        self.pars = [-1] * n
    def find(self, x):
        if self.pars[x] < 0:
            return x
        else:
            oya = self.pars[x]
            return self.find(oya)
            #self.pars[x] = self.find(oya)
            #return self.pars[x]
    def union(self, x, y):
        X = self.find(x)
        Y = self.find(y)
        if X == Y: return
        if self.pars[X] > self.pars[Y]:
            X, Y = Y, X

        self.pars[X] += self.pars[Y]
        self.pars[Y] = X

#https://leetcode.com/problems/is-graph-bipartite/discuss/445182/my-cpp-union-find-solution
class Solution_unionfind:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if graph is None: return False
        N = len(graph)
        if N <= 1: return True
        uf = unionfind(N)
        #print(uf.pars)
        whole = {i for i in range(N)}
        for i in range(N):
            for j in range(len(graph[i])):
                if uf.find(i) == uf.find(graph[i][j]):
                    return False
                if j > 0:
                    uf.union(graph[i][j], graph[i][j-1])
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # coloring
        # https://www.youtube.com/watch?v=Gmp51E8HVVs
        if graph is None: return False
        if len(graph) <= 1: return True

        colors = [0] * len(graph)

        def dfs(i, color): # trying to color the node
            if colors[i] != 0:
                return colors[i] == color
            else:
                colors[i] = color
                for j in graph[i]:
                    if dfs(j, -color) == False:
                        return False
            return True

        for i in range(len(graph)):
            if colors[i] == 0 and dfs(i, 7) == False:
                return False
        return True






        pass

samples = [
    [[1,3], [0,2], [1,3], [0,2]],
    [[1],[0,3],[3],[1,2]]
]

for S in samples:
    ans = Solution().isBipartite(S)
    print(ans)

