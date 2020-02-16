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



class Solution_bottomup:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        それぞれのi,jまでの範囲ででの最大をだしていく。
        つまりdp[i][j]は範囲を右下をi,jとした時の最大面積は？という価値関数になる。
        状態は、0か1のどちらか
        0の場合は、0となる。これまでの最高を引鶴と、うまく行かないのは自明。
        だから1の場合は、上、左、左上の３店のminに1を加える
        とここまでいうと
        dp[i][j]は範囲を右下をi,jとした時、右下を含む範囲全体の最大面積は？という価値関数になる。
        なので、毎回dp[i][j]を計算していって、maxを更新する作業O(1)が必要です
        """
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        maxi = 0
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            maxi = max(dp[i][0], maxi)
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
            maxi = max(dp[0][j], maxi)

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = 0 if matrix[i][j] == "0" else min(
                    dp[i-1][j-1],
                    dp[i][j-1],
                    dp[i-1][j]
                ) + 1
                maxi = max(dp[i][j]**2, maxi)
        return maxi

#https://www.byte-by-byte.com/squaresubmatrix/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions
#この辺で、@lru_cacheつかってみたいから。
class Solution_tle: # topdown
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        maxi = 0

        def square_matrix(matrix, i, j):
            if i >= n or j >= m: return 0
            if matrix[i][j] == "0": return 0
            return 1 + min(
                square_matrix(matrix, i+1, j),
                square_matrix(matrix, i  , j+1),
                square_matrix(matrix, i+1, j+1),
            )

        for i in range(0, n):
            for j in range(0, m):
                local = square_matrix(matrix, i, j)
                maxi = max(local**2, maxi)
        return maxi


from functools import lru_cache
class Solution: # topdown
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        maxi = 0

        @lru_cache(maxsize=None)
        def square_matrix(i, j):
            if i >= n or j >= m: return 0
            if matrix[i][j] == "0": return 0
            return 1 + min(
                square_matrix(i+1, j),
                square_matrix(i  , j+1),
                square_matrix(i+1, j+1),
            )

        for i in range(0, n):
            for j in range(0, m):
                local = square_matrix(i, j)
                maxi = max(local**2, maxi)
        return maxi


samples = [
    # (
    #     [
    #         ["1", "0", "1", "0", "0"],
    #         ["1", "0", "1", "1", "1"],
    #         ["1", "1", "1", "1", "1"],
    #         ["1", "0", "0", "1", "0"],
    #     ]
    # ),
    (
        [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]]
    )

]
for S in samples:
    ans = Solution().maximalSquare(S)
    print(ans)
