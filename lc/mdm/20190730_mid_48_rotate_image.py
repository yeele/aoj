#-*- coding: utf-8 -*-
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                tmp = matrix[r][c]





matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


Solution().rotate(matrix)
print(matrix)