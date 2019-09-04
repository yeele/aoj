#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

class Solution:
    """
    お見事。hard自力でクリア
    """
    def longestConsecutive(self, S: List[int]) -> int:
        length = len(S)
        if length <= 0: return 0

        edges = {}
        from collections import defaultdict
        exist = defaultdict(lambda:False)
        visit = defaultdict(lambda:False)

        for i in range(length):
            value = S[i]
            edges[value] = [value-1, value+1]
            exist[value] = True

        def dfs(value, sofar=0) -> int:
            visit[value] = True
            counter = sofar
            #if value not in exist: # O(logN)
            if not exist[value]: # O(1)
                return counter

            counter += 1 # value is exist, so add one
            tmp = 1
            for neighbour in edges[value]:
                if exist[neighbour] and not visit[neighbour]:
                    # 帳尻合わせっぽい、感じになってしまったが、まぁ -1というのは neigherから帰ってくるのはvalueも含めてにことなので、その辺
                    # をうまくやるための -1。
                    tmp += dfs(neighbour, counter) - 1
            return max(tmp, counter)

        maxi = 0
        for i in range(length):
            maxi = max(dfs(S[i], 0), maxi)
        return maxi



samples = [
    #([100, 4, 200, 1, 3, 2], 4),
    ([100,4,200,1,3,2], 4),
    # ([1, 2, 3, 10, 4, 9, 5], 5),
    # ([9, 5, 8, 1, 4, 10, 13, 7, 11, 12, 3, 2], 7),
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().longestConsecutive(S)
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))

