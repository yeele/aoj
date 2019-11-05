#-*- coding: utf-8 -*-
from typing import List
import logging

#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution_puedo:
    def containVirus(self, grid: List[List[int]]) -> int:

        #1 fil infected candidate -1 and decrement

        #2 dfs on 1 region and identify max -1
        # break if there's only one region to save.

        #3 add the max on your walls_count
        # walls can be expressed with 2.

        #4 apply the infection except for the maxed region

        # repeat

        #(explanation) O(N)*4, (49 at most)
        # 50*4 = 200 , 200 * 50 = 10000なのでoK
        # さぁ実装するぞ 8:32am

        return 0


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        def print_grid(S):
            for row in S:
                for element in row:
                    print("%3d" % element, end=",")
                print("")
        visitted = [[0]*n for _ in range(m) ]
        def d4_generator(i, j):
            #       left   ,  right ,  up,    down
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for h, v in dirs:
                _i = i + h
                _j = j + v
                if valid(_i, _j):
                    yield (_i, _j)

        def valid(i, j) -> bool:
            if i < 0 or i >= m: return False
            if j < 0 or j >= n: return False
            return True
        #1 fil infected candidate -1 and decrement
        def bfs(i, j):
            stack = set() # Use set to not to have duplicadted. otherwise, it could, e.g.,)
            # (2, 7) could be added from (1, 7) and (2, 6) and as 2, 7 has not been visitted neither points.
            stack.add((0, 0))
            while len(stack) > 0:
                coordinate = stack.pop()
                (x, y) = coordinate
                if grid[x][y] == 1:
                    for _i, _j in d4_generator(x, y):
                        if grid[_i][_j] <= 0:
                            # candidate of wall
                            grid[_i][_j] -= 1
                visitted[x][y] = 1
                tmp = list(d4_generator(x, y))
                for _i, _j in d4_generator(x, y):
                    if visitted[_i][_j] == 0:
                        stack.add((_i, _j))


        bfs(0, 0)
        print_grid(grid)
        print('---- visitted -----')
        print_grid(visitted)
        #2 dfs on 1 region and identify max -1
        # break if there's only one region to save.

        visitted = [[0]*n for _ in range(m) ] # reset visitted
        stack = []
        ones = []
        stack.append((0, 0))
        max_wall = 0
        max_cordinate = (-1, -1)
        while len(stack) > 0:
            coordinate = stack.pop()
            (x, y) = coordinate
            visitted[x][y] = 1
            if grid[x][y] == 1:
                stack2 = [(x, y)]
                ones.append((x, y))
                local = set()
                while len(stack2):
                    coordinate2 = stack2.pop()
                    (x2, y2) = coordinate2
                    for _i, _j in d4_generator(x2, y2):
                        if grid[_i][_j] < 0:
                            local.add((_i, _j))
                        else:
                            if visitted[_i][_j] == 0:
                                stack2.append((_i, _j))
                        visitted[_i][_j] = 1
                local_walls = sum([abs(grid[__i][__j]) for __i, __j in ones])
                if local_walls > max_wall:
                    max_wall = local_walls
                    max_cordinate = (x, y)
            for _i, _j in d4_generator(x, y):
                if visitted[_i][_j] == 0:
                    stack.append((_i, _j))
        print("max_wall:%s, max_cordiate:%s" % (max_wall, max_cordinate))

        #3 add the max on your walls_count
        # walls can be expressed with 2.

        #4 apply the infection except for the maxed region

        # repeat

        #(explanation) O(N)*4, (49 at most)
        # 50*4 = 200 , 200 * 50 = 10000なのでoK
        # さぁ実装するぞ 8:41am

        return 0

samples = [
    (
        [[0,1,0,0,0,0,0,1],
         [0,1,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0]], 10
    ),

    (
        [[1,1,1],
         [1,0,1],
         [1,1,1]], 4
    )
]


for S, expected in samples:
    ans = Solution().containVirus(S)
    print(ans)
