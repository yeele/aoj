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


class Solution_me:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        最大をもとめたい。
        BFはすべての点を操作して、そこをスタートポイントしたときに、四角ができるか操作する
        なのでO(M*N) * O(M*N)かかる,いわゆるO(N^4)だ。
        なので問題を最小化して、なにかできないか？と考える。
        ４角を構成するためには、左、左上、右上を知っていればいいので
        さらに、縦横の連続値を保存しておく(h, w)としよう
        つまり
        dpを用意しておいて
        dp[i][j] =
          ここ(i,j)が1だったら
          縦は = dp[i-1][j]上の縦に+1
          横は = dp[i][j-1]上の横に+1
        """
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        dph = [ [0] * m for _ in range(n) ]
        dpw = [ [0] * m for _ in range(n) ]
        dph2 = [ [0] * m for _ in range(n) ]
        dpw2 = [ [0] * m for _ in range(n) ]
        def valid(i, j):
            if i < 0 or i >= n: return False
            if j < 0 or j >= m: return False
            return True
        def get(dp, i, j):
            if valid(i, j): return dp[i][j]
            else: return 0

        # ----main----------------
        maxi = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dph[i][j] = get(dph, i-1, j) + 1
                    dpw[i][j] = get(dpw, i, j-1) + 1
                    dph2[i][j] = get(dph2, i-1, j) + 1
                    dpw2[i][j] = get(dpw2, i, j-1) + 1
                    if get(dph, i-1, j-1) == 0:
                        dph2[i][j] = 1
                    if get(dpw, i-1, j-1) == 0:
                        dpw2[i][j] = 1

                if get(dph, i-1, j-1) > 0 and get(dpw, i-1, j-1) > 0:
                    local = dph2[i][j] * dpw2[i][j]
                else:
                    local = max(dph2[i][j], dpw2[i][j])
                maxi = max(maxi, local, dph[i][j], dpw[i][j])
        print("---- dph ----")
        for row in dph2: print(row)
        print("---- dpw ----")
        for row in dpw2: print(row)
        return maxi


"""
むずかしい！
https://www.cnblogs.com/grandyang/p/4550604.html
と
https://andreswang.com/2019/03/21/maximal-rectangle/
をよんでも、

まだ理解でいない
最終的に
https://www.youtube.com/watch?v=g8bSdXCG-lA
ツシャーの動画でわかった。ちょっと違う解法だけど。
"""

class Solution_me:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass


samples = [
    # (
    #     [
    #         ["1","0","1","0","0"],
    #         ["1","0","1","1","1"],
    #         ["1","1","1","1","1"],
    #         ["1","0","0","1","0"]
    #     ]
    # ),
    # (
    #     [
    #         ["1","1"]
    #     ]
    # ),
    (
        [
            ["0","1","1","0","1"],
            ["1","1","0","1","0"],
            ["0","1","1","1","0"],
            ["1","1","1","1","0"],
            ["1","1","1","1","1"],
            ["0","0","0","0","0"]]
    )

]
for S in samples:
    ans = Solution().maximalRectangle(S)
    print(ans)
