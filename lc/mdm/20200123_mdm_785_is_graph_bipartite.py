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

class unionfind():
    def __init__(self, n):
        self.n = n
        # pars means parents
        # it tells you parent of given index
        # if index is 3. and pars[3] is 0, that means 3's parent is 0.
        # if pars[3] is negative value, it means 3 itself is parent( it's the root)
        # and the abs value is the number of nodes in that group
        self.pars = [-1] * n

    def find(self, x):
        if self.pars[x] < 0:
            return x
        else:
            # 親が根元ではないので、根元を探す旅
            oya = self.pars[x]
            #なんかこのアップデートは、トリッキーでこれが経路圧縮なのか？！
            #　なくてもうごくと思っている。
            # self.pars[x] = self.find[oya]; return self.pars[x]
            return self.find(oya)

    def union(self, x, y):
        X = self.find(x) # Xはxの親である
        Y = self.find(y)
        # それぞれの親が登頂しましたね。
        if X == Y: return

        # 親が違うのでまーじしましょう。
        # 親のグループの小さい方に、大き方を足したいので。
        if self.pars[X] > self.pars[Y]:
            X, Y = Y, X

        self.pars[X] += self.pars[Y]
        self.pars[Y] = X


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = unionfind(len(graph))
        wholeset = {i for i in range(len(graph))}
        for i, nodes in enumerate(graph):
            for j in wholeset - set(nodes + [i]):
                # i j is in same group :)
                print("i:%s and j:%s are in other island" % (i, j))
                uf.union(i, j)
        print("pars looks like %s" % uf.pars)
        return graph

samples = [
    [[1,3], [0,2], [1,3], [0,2]]
]
for S in samples:
    ans = Solution().isBipartite(S)
    print(ans)
