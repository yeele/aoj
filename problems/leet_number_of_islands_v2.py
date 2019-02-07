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
"""

input_data = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        id = 0
        islands = 0
        db = {}
        row_sz = len(grid)
        col_sz = len(grid[0]) if row_sz > 0 else 0
        for i in range(row_sz):
            for j in range(col_sz):
                cur = grid[i][j]
                if cur == "1":
                    if j+1 < col_sz and (i, j+1) in db:
                        pass
                    elif not (i,j) in db:
                        id += 1
                    else:
                        pass
                    db[(i,j)] = id
                    if j+1 < col_sz and grid[i][j+1] == "1": db[(i,j+1)] = id
                    if i+1 < row_sz and grid[i+1][j] == "1": db[(i+1,j)] = id

        return len(set(db.values()))


logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
#logging.getLogger().setLevel(logging.INFO)
#logging.debug(Vert("0,3", 1))

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
islands = Solution().numIslands(grid)
logging.info("%s" % islands)