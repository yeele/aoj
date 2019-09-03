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
    """
    へー、一回こたえ、
    他の人のソリューションをみましたので、それをふまえて再実装といきやす
    自分の考えに近かった。そして自分は実装しきれなかった
    アトランティスとパシフィックをにそれぞれ到達したかを確認する
    アルゴリズムで行ってみます
    """
    def pacificAtlantic(self, S: List[List[int]]) -> List[List[int]]:
        m = len(S)
        if m == 0: return []
        n = len(S[0])

        def print_matrix(matrix:List[List[int]]):
            for row in matrix:
                logging.debug(row)

        # inspired from https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/365921/Search-in-Python
        # def neighbours(i, j):
        #     directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        #     nbs = []
        #     for arrow in directions:
        #         x, y = arrow
        #         if 0 <= i+x < n:
        #             if 0 <= j+y < m:
        #                 nbs.append((i+x, j+y))
        #     return nbs
        def neighbours(i, j):
            return [
                (i + a, j + b)
                for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= i + a < m
                if 0 <= j + b < n
            ]
        def dfs(i, j, visited):
            logging.debug("dfs(%s, %s, visited)" % (i, j))
            if visited[i][j]: return
            visited[i][j] = True
            nbs = neighbours(i, j)
            logging.debug("neighbors(i:%s, j:%s) => %s" % (i, j, nbs))
            for r, c in nbs:
                logging.debug("r:%s, c:%s, i:%s, j:%s" % (r, c, i, j))
                if S[r][c] >= S[i][j]:
                    dfs(r, c, visited)
                    logging.debug("miso1")
            logging.debug("miso2(r:%s, c:%s)" % (r, c))

        ans = []
        pacific  = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append((i, j))
        logging.debug("---- pacific ----")
        print_matrix(pacific)
        logging.debug("---- atlantic ----")
        print_matrix(atlantic)
        logging.debug("---- S ----")
        print_matrix(S)
        return ans


samples = [
    # (
    #     [
    #         [1, 2, 2, 3, 5],
    #         [3, 2, 3, 4, 4],
    #         [2, 4, 5, 3, 1],
    #         [6, 7, 1, 4, 5],
    #         [5, 1, 1, 2, 4],
    #     ],
    #     [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    # ),
    # (
    #     [[1,1],[1,1],[1,1]],
    #     [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
    # ),
    (
        [[3,3,3,3,3,3],[3,0,3,3,0,3],[3,3,3,3,3,3]],
        [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,2],[1,3],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5]]
    )
]

for S, expected in samples:
    print("-"*20)
    ans = Solution().pacificAtlantic(S)
    assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))
