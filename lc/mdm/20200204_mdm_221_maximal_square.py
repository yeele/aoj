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



class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def is_range(matrix, i, j):
            N = len(matrix)
            M = len(matrix[0])
            if i < 0 or i >= N: return False
            if j < 0 or j >= M: return False
            return True

        def validate(matrix, h, w, length):
            for n in range(length):
                for m in range(length):
                    i, j = h + n, w + m
                    if matrix[i][j] != 1:
                        return False
            return True

        def get_max_square(matrix, x, y):
            counter = 0
            i, j = x, y
            while is_range(matrix, i, j) and matrix[i][j] == 1:
                if validate(matrix, x, y, counter):
                    counter += 1
                i += 1
                j += 1
            return counter ** 2

        def solve(matrix: List[List[int]]) -> int:
            N = len(matrix)
            if N == 0: return 0
            M = len(matrix[0])
            maxi = 0
            for i in range(N):
                for j in range(M):
                    local = get_max_square(matrix, i, j)
                    maxi = max(local, maxi)
            return maxi
        matrix2 = [list(map(int, row)) for row in matrix]
        return solve(matrix2)



samples = [
    (
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
    )

]
for S in samples:
    ans = Solution().maximalSquare(S)
    print(ans)
