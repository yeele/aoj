#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
from typing import List
from collections import defaultdict
import sys, time

def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # edge
        if len(equations) != len(values) or len(values) == 0: return []
        graph = defaultdict(dict)
        def make(graph, equation, value):
            (x, y) = equation
            graph[x].update({y:value}) # Todo. not to use udpate, but graph[x][y] = value, is faster
            graph[y].update({x:1/value})

        for i in range(len(values)):
            make(graph, equations[i], values[i])


        def bfs(start, end):
            visited = defaultdict(int)
            stack = [(start, 1)]
            while stack:
                n, acc = stack.pop()
                if visited[n] == 1: continue
                if n == end: return acc if n in graph else -1.0
                for j, value in graph[n].items():
                    stack.append((j, value * acc))
                visited[n] = 1
            return -1

        A = []
        for a, b in queries:
            A.append(bfs(a, b))
        return A

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

ans = Solution().calcEquation(equations, values, queries)
print(ans)