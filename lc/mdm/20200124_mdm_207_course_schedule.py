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

from collections import defaultdict
class Solution:
    def canFinish(self, n: int, S: List[List[int]]) -> bool:
        if n <= 1: return True
        if S is None or len(S) == 0: return True
        graph = defaultdict(list)
        for cons in S:
            graph[cons[0]].append(cons[1])

        visited = {i: 0 for i in range(n)}
        def cyclic(i):
            if visited[i] == 2: return False
            if visited[i] == 1: return True
            visited[i] = 1
            for j in graph[i]:
                if cyclic(j) == True: return True
            visited[i] = 2
            return False

        counter = 0
        for i in range(n):
            if not cyclic(i): counter += 1
        print(counter)
        return counter == n


samples = [
    (2, [[0, 1], [1,0]]),
    (2, [[1, 0]]),
]
for n, S in samples:
    ans = Solution().canFinish(n, S)
    print(ans)
