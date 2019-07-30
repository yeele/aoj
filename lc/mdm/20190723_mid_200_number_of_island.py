#-*- coding: utf-8 -*-
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        #self.print(S)
        for i, row in enumerate(S):
            for j, s in enumerate(row):
                #print(s, S[i][j])
                if s == '1':
                    num += 1
                    ##print('-'*8)
                    self.explore(S, i, j)
                    #sself.print(S)
                else:
                    pass

        return num

    def print(self, S):
        for row in S:
            print(row)

    def get(self, S, i, j):
        try:
            if i < 0 or j < 0: return None
            else: return S[i][j]
        except:
            return None

    def explore(self, S, i, j):
        stack = []
        stack.append((i, j))
        while len(stack) > 0:
            i, j = stack.pop()
            for ni, nj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if self.get(S, ni, nj) == '1':
                    stack.append((ni, nj))
            S[i][j] = '0' # overwrite


# after watching some video,
# same solution, but bit cleaner and less memory solution here
# https://leetcode.com/problems/number-of-islands/discuss/341462/Python-solution-(simple)
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sinkIsland(grid, r, c):
            if (r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0]) or
                grid[r][c] != '1'
            ):
                return
            else: # means grid[r][c] is 1
                grid[r][c] = '#'
                sinkIsland(grid, r-1, c)
                sinkIsland(grid, r+1, c)
                sinkIsland(grid, r, c-1)
                sinkIsland(grid, r, c+1)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    counter += 1
                    sinkIsland(grid, i, j)
        return counter




S_raw = [
    "11110",
    "11010",
    "11000",
    "00000"
    ]

S = [ list(row) for row in S_raw ]
S = [["1","0","1","1","0","1","1"]]
print(Solution().numIslands(S))
S = [["1","0","1","1","0","1","1"]]
print(Solution2().numIslands(S))

