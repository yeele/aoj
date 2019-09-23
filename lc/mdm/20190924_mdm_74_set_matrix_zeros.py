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



from collections import defaultdict
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first path, remember where are zeros, as memo
        # second round, overwrite based on the memo
        rows = defaultdict(lambda: -1)
        cols = defaultdict(lambda: -1)
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0





samples = [
    # 0820am
    (
        [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ],
        [
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ]
    )
    # 0831am succeeded.
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
    ans = Solution().setZeroes(S)
    logging.debug("after:\n%s" % S)
    #print(ans)
