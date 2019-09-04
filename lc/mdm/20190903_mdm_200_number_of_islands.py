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
    def numIslands(self, S: List[List[str]]) -> int:
        m = len(S)
        if m == 0: return 0
        n = len(S[0])
        visit = [ [False] * n for _ in range(m) ]

        # def neighbours(i, j):
        #     directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        #     nbs = []
        #     for h, v in directions:
        #         if 0 <= i + v < n and 0 <= j + h < m:
        #             nbs.append((i+v, j+h))
        #     return nbs
        def neighbours(i, j):
            return [
                (i + a, j + b)
                for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= i + a < m
                if 0 <= j + b < n
            ]

        # dfsのポイント！親にもどらないようにしないと永遠に再帰する
        def dfs_forever(i, j, sofar=0):
            ttl = sofar
            if S[i][j] == '1':
                for v, h in neighbours(i, j):
                    if not visit[v][h]:
                        ttl += dfs(v, h, sofar+1)
            #visit[i][j] == True # わぉ！、こんなミスが！！！　（その後下のように変更修正)　まぁ、それでも永遠再帰には変わりないw
            visit[i][j] = True #
            return ttl

        # dfsのポイント！親にもどらないようにしないと永遠に再帰する
        def dfs_still_forever(i, j, parent:tuple = None, sofar=0):
            ttl = sofar
            if S[i][j] == '1':
                for v, h in neighbours(i, j):
                    if not visit[v][h]:
                        if parent == None or parent != (i, j):
                            ttl += dfs(v, h, (i, j), sofar+1)
            visit[i][j] == True
            return ttl
        # dfsのポイント！そうじゃないんだ！visitフラッグのタイミングを冒頭にすればいいだけなんだ！
        # しかし、ほぼ正解なんだが、[[1]]などのエッジケースでとりこぼすぞ！
        def dfs_edge(i, j, sofar=0):
            visit[i][j] = True
            ttl = sofar
            if S[i][j] == '1':
                for v, h in neighbours(i, j):
                    if not visit[v][h]:
                        ttl += dfs(v, h, sofar+1)
            return ttl

        # うえのようなエッジケースをカバーした正解dfsがこちら
        # ttlに最初に+1しているのが、変更点です。おわかりいただけただろうか。
        def dfs(i, j, sofar=0):
            visit[i][j] = True
            ttl = sofar
            if S[i][j] == '1':
                ttl += 1
                for v, h in neighbours(i, j):
                    if not visit[v][h]:
                        ttl += dfs(v, h, ttl)
            return ttl

        ans = 0
        for i in range(m):
            for j in range(n):
                if not visit[i][j]:
                    if dfs(i, j) > 0:
                        ans += 1
        return ans

samples = [
    (
        [
            [1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0],
        ], 1
    ),
    (
        [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1],
        ],
        3
    )
]

for S, expected in samples:
    print("-"*20)
    S = [list(map(lambda x: str(x), row)) for row in S]
    ans = Solution().numIslands(S)
    assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))
