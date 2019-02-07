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
"""
class Vert:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.adjs = []
        self.visited = False
    def visit(self):
        logging.debug("visiting %s" % self.key)
        self.visited = True

    def __str__(self):
        return "Vert: key(%s), value(%s), adjs(%s)" % (self.key, self.value, self.adjs)

input_data = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

def get_graph(input_data):
    if input_data is None: return []
    if len(input_data) == 0: return []
    col_sz = len(input_data[0])
    row_sz = len(input_data)
    def exist(input_data, i, j):
        try:
            if i < 0 or j < 0: return False # out of bound
            if input_data[i][j] == "1": return True
        except Exception as e:
            pass
        return False

    graph = []
    for i in range(row_sz):
        row = []
        for j in range(col_sz):
            value = input_data[i][j]
            v = Vert("%s,%s" % (i, j), value)
            if value == "1":
                if exist(input_data, i, j+1): v.adjs.append("%s,%s" % (i, j+1))
                if exist(input_data, i, j-1): v.adjs.append("%s,%s" % (i, j-1))
                if exist(input_data, i+1, j): v.adjs.append("%s,%s" % (i+1, j))
                if exist(input_data, i-1, j): v.adjs.append("%s,%s" % (i-1, j))
            row.append(v)
        graph.append(row)
    return graph

def traverse(cur, graph):
    # cur: Vert, graph: list[Vert]
    if cur is None: return
    if cur.visited: return
    cur.visit()
    for key in cur.adjs:
        #logging.debug("key:%s" % key)
        i = int(key.split(",")[0])
        j = int(key.split(",")[1])
        #logging.debug("i:%s, j:%s" % (i,j))
        next_vert = graph[i][j]
        #logging.debug("next_vert:%s" % next_vert)
        traverse(next_vert, graph)

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        trees = 0
        islands = 0
        #graph = get_graph(input_data)
        graph = get_graph(grid)
        for row in graph:
            for e in row:
                logging.debug("==== traverse by %s =================" % e)
                if not e.visited and e.value == "1":
                    logging.debug("!!!!!!! traverse by %s !!!!!!!!!!!!!!!!!!!!!" % e.key)
                    trees += 1
                traverse(e, graph)
        return trees


logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
#logging.getLogger().setLevel(logging.INFO)
#logging.debug(Vert("0,3", 1))

# grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# trees = Solution().numIslands(grid)
#logging.info("%s" % trees)