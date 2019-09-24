#-*- coding: utf-8 -*-
from typing import List
import math

import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return matrix
        if len(matrix[0]) == 0: return []

        m = len(matrix)
        n = len(matrix[0])
        visitted = [[0] * n for _ in range(m)]
        #                 right,  down ,  left   , up
        direction_set = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def change_direction(direction):
            direction += 1
            if direction == 4:
                direction = 0
            return direction
        def get_next(i, j, direction):
            arrow = direction_set[direction]
            i_ = i + arrow[0]
            j_ = j + arrow[1]
            if i_ < 0 or j_ < 0 or i_ >= m or j_ >= n or visitted[i_][j_] == 1:
                direction = change_direction(direction)
                arrow = direction_set[direction]
                i_ = i + arrow[0]
                j_ = j + arrow[1]
                if i_ < 0 or j_ < 0 or i_ >= m or j_ >= n or visitted[i_][j_] == 1:
                    return (None, i_, j_, direction) # end
                else:
                    visitted[i_][j_] = 1
                    return (matrix[i_][j_], i_, j_, direction)

            else:
                visitted[i_][j_] = 1
                return (matrix[i_][j_], i_, j_, direction)

        path = []
        i = 0
        j = -1
        direction = 0
        for _ in range(m*n):
            (value, i, j, direction) = get_next(i, j, direction)
            if value == None: break
            path.append(value)

        return path



samples = [
    # 0841am
    (
        [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ],
        [1,2,3,6,9,8,7,4,5]
    )
    # 0917am succeeded. (36 mins elapsed)
]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)
import logging
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
for S, expected in samples:
    ans = Solution().spiralOrder(S)
    print(ans)
