#-*- coding: utf-8 -*-
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:
Input:
11000
11000
00100
00011

Output: 3
"""
import logging

"""
Solution 1: use Graph traversal. O(N) + O(N) for graph traversal DFS
Solution 2: O(N) passing current count and island identifier
Solution 3: traverse , but no class (https://www.youtube.com/watch?v=o8S2bO3pmO4) 
"""

input_data = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]


class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0': return 0
        grid[i][j] = '0'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        return 1

    def numIslands(self, grid):
        #if grid is None or len(grid) <= 0: return 0
        islands = 0
        row_sz = len(grid)
        col_sz = len(grid[0]) if row_sz > 0 else 0
        for i in range(row_sz):
            for j in range(col_sz):
                cur = grid[i][j]
                if cur == '1':
                    islands += self.dfs(grid, i, j)
        return islands


logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
#logging.getLogger().setLevel(logging.INFO)
#logging.debug(Vert("0,3", 1))

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
logging.info("%s" % Solution().numIslands(grid))