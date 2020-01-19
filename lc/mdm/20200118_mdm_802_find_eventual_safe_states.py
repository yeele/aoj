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

class Solution_mine_wrong:
    def single(self, graph, start, cache={}) -> bool: # start = 0
        if graph is None: return False
        stack = [start]
        visited = [0] * len(graph)
        safe    = [0] * len(graph)
        while stack: # [2, 5]
            idx = stack.pop() # 5
            #if idx in cache: return cache[idx]
            if visited[idx] == 0: # visited = [1,1,1,1,0,1,0]
                for next_idx in graph[idx]: # [5]
                    if next_idx in visited and safe[next_idx]:
                        return False
                    stack.append(next_idx)
                visited[idx] = 1
                if len(graph[idx]) == 0:
                    safe[idx] = 1
            else:
                if safe[idx] == 0: return False
        return True
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if len(graph) == 0: return []
        A = []
        memo = {}
        for i, nodes in enumerate(graph):
            if self.single(graph, i, memo):
                A.append(i)
                memo[i] = True
            else:
                memo[i] = False
        return A
# https://leetcode.com/problems/find-eventual-safe-states/solution/
import collections
class Solution_lc(object):
    def eventualSafeNodes(self, graph):
        N = len(graph)
        safe = [False] * N

        print(graph)
        graph = map(set, graph)

        rgraph = [set() for _ in range(N)]
        print(rgraph)
        # q = collections.deque()
        #
        # for i, js in enumerate(graph):
        #     if not js:
        #         q.append(i)
        #     for j in js:
        #         rgraph[j].add(i)
        #
        # while q:
        #     j = q.popleft()
        #     safe[j] = True
        #     for i in rgraph[j]:
        #         graph[i].remove(j)
        #         if len(graph[i]) == 0:
        #             q.append(i)
        #
        # return [i for i, v in enumerate(safe) if v]

class Solution_working_but_LTE():
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

# let's improve Solution_working_but_LTE
class Solution():
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

S = [[1,2],[2,3],[5],[0],[5],[],[]]
#S = [[],[0,2,3,4],[3],[4],[]]
ans = Solution().eventualSafeNodes(S)
print(ans)
