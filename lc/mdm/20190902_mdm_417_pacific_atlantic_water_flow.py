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

"""
方向性は悪くないはずだが
うまく、考えれなくなってきたので、一回このファイルではなくて
新しいファイルで実装しなおすわ。
なのでこのファイルはこのまま保存しておく
"""
class Solution:
    def pacificAtlantic(self, S: List[List[int]]) -> List[List[int]]:
        m = len(S)
        if m == 0: return []
        n = len(S[0])

        dp = [ [-1] * n for _ in range(m) ]
        done = [ [0] * n for _ in range(m) ]
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
            if (i == 0 or j == 0) and (i == (m-1) or j == (n-1)):
                dp[i][j] = 3
                done[i][j] = 1
                return dp[i][j]
            if i == (m-1) or j == (n-1):
                dp[i][j] = max(2, dp[i][j])
                done[i][j] = 1
                return dp[i][j]
            if i == 0 or j == 0:
                dp[i][j] = max(1, dp[i][j])
                done[i][j] = 1
                return dp[i][j]

            if done[i][j] == 1: return dp[i][j]


            if idx_valid(i, j-1) and S[i][j-1] <= S[i][j]: dfs(i, j-1)
            if idx_valid(i, j+1) and S[i][j+1] <= S[i][j]: dfs(i, j+1)
            if idx_valid(i+1, j) and S[i+1][j] <= S[i][j]: dfs(i+1, j)
            if idx_valid(i-1, j) and S[i-1][j] <= S[i][j]: dfs(i-1, j)
            #　でも実はまだ上下左右のdpは計算中の可能性がある
            complete = [0, 0, 0, 0]
            def completeness_check(i, j, delta_i, delta_j):
                if idx_valid(i+(delta_i), j+(delta_j)) and S[i+(delta_i)][j+(delta_j)] <= S[i][j]:
                    return done[i+(delta_i)][j+(delta_j)]
                else:
                    return 1

            complete[0] = completeness_check(i, j,  0, -1)
            complete[1] = completeness_check(i, j,  0,  1)
            complete[2] = completeness_check(i, j,  1,  0)
            complete[3] = completeness_check(i, j, -1,  0)

            done[i][j] = 1 if sum(complete)==4 else 0

            l = dp_get(i, j-1)
            r = dp_get(i, j+1)
            u = dp_get(i+1, j)
            b = dp_get(i-1, j)
            if max(l, r, u, b) == 3:
                dp[i][j] = 3
                done[i][j] = 1
            if 1 in [l, r, u, b] and 2 in [l, r, u, b]:
                dp[i][j] = 3
                done[i][j] = 1
            else:
                dp[i][j] = max(0, l, r, u, b)

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
        logging.debug("---- done ----")
        print_matrix(done)
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
