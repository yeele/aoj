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


class Solution:
    def pacificAtlantic(self, S: List[List[int]]) -> List[List[int]]:
        m = len(S)
        if m == 0: return []
        n = len(S[0])

        dp = [ [-1] * n for _ in range(m) ]
        done = [ [False] * n for _ in range(m) ]
        # -1, not visitted
        #  0 = none, 1 = ~, 2 = *, 3 = ~ and *
        def idx_valid(i, j):
            if i < 0 or i >= m: return False
            if j < 0 or j >= n: return False
            return True
        def dp_get(i, j, default=-1):
            if idx_valid(i, j): return dp[i][j]
            return default
        def print_matrix(matrix:List[List[int]]):
            for row in matrix:
                logging.debug(row)

        def dfs(i, j):
            logging.debug("dfs(%s, %s)" % (i, j))
            #if dp[i][j] >= 0: return dp[i][j]
            if i == 0 or j == 0: dp[i][j] = 1
            if i == (m-1) or j == (n-1): dp[i][j] = 2
            if (i == 0 or j == 0) and (i == (m-1) or j == (n-1)): dp[i][j] = 3
            if dp[i][j] > 0:
                done[i][j] = True
                return dp[i][j]

            if idx_valid(i, j-1) and S[i][j-1] <= S[i][j]: dfs(i, j-1)
            if idx_valid(i, j+1) and S[i][j+1] <= S[i][j]: dfs(i, j+1)
            if idx_valid(i+1, j) and S[i+1][j] <= S[i][j]: dfs(i+1, j)
            if idx_valid(i-1, j) and S[i-1][j] <= S[i][j]: dfs(i-1, j)
            #　でも実はまだ上下左右のdpは計算中の可能性がある
            l = dp_get(i, j-1)
            r = dp_get(i, j+1)
            u = dp_get(i+1, j)
            b = dp_get(i-1, j)
            if max(l, r, u, b) == 3:
                dp[i][j] = 3
            if 1 in [l, r, u, b] and 2 in [l, r, u, b]:
                dp[i][j] = 3
            else:
                dp[i][j] = max(0, l, r, u, b)
            # 周りが有効な状態で計算しきったかどうか。
            if min(l, r, u, b) == -1: done[i][j] = False
            else: done[i][j] = True

            return dp[i][j]

        ans = []
        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    local = dfs(i, j)
                    if local >= 2:
                        ans.append([i, j])
        logging.debug("---- dp ----")
        print_matrix(dp)
        logging.debug("---- S ----")
        print_matrix(S)
        return ans



samples = [
    (
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    )
]

for S, expected in samples:
    print("-"*20)
    ans = Solution().pacificAtlantic(S)
    #assert ans == expected, "(%s) => %s but %s was expected" % (k, S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))
