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

import math
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        if length == 0: return matrix
        #repeat = math.ceil(length/2)
        repeat = length // 2 if length%2==0 else length // 2 + 1
        for i in range(repeat):
            sz = length - (i*2)
            #print(i, i)
            print("-"*64)
            for n in range(sz-1):
                j = i + n
                print(i, j)
                l = j - i
                r = (i + sz) - j - 1
                # swap
                i_ = i+l
                j_ = j+r
                tmp2 = matrix[i_][j_] # O2
                matrix[i_][j_] = matrix[i][j] # O2 <-- O1
                i_ = i_+r
                j_ = j_-l
                tmp3 = matrix[i_][j_] # O3
                matrix[i_][j_]= tmp2 # O3  <-- O2
                i_ = i_-l
                j_ = j_-r
                tmp4 = matrix[i_][j_] # O4
                matrix[i_][j_] = tmp3 # O4 <-- O3
                matrix[i][j] = tmp4     # O1 <-- O4







samples = [
    # 1954pm start
    # 2142pm thinking finish
    # 2142pm
    # (
    #     [
    #         [1,2,3],
    #         [4,5,6],
    #         [7,8,9]
    #     ],
    #     [
    #         [7,4,1],
    #         [8,5,2],
    #         [9,6,3]
    #     ]
    # ),
    # (
    #     [
    #         [ 5, 1, 9,11],
    #         [ 2, 4, 8,10],
    #         [13, 3, 6, 7],
    #         [15,14,12,16]
    #     ],
    #     [
    #         [15,13, 2, 5],
    #         [14, 3, 4, 1],
    #         [12, 6, 8, 9],
    #         [16, 7,10,11]
    #     ]
    # )
    # 2231pm
    # 6/21 failed
    (
        [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]],
        [[4,33,13,32,12,2],[24,1,14,33,27,29],[1,20,32,32,9,20],[6,7,27,2,25,26],[32,21,22,28,13,16],[34,7,26,14,21,28]]
    )
]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)
import logging
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
for S, expected in samples:
    logging.debug("before:\n%s" % S)
    ans = Solution().rotate(S)
    logging.debug("after:\n%s" % S)
    #print(ans)
