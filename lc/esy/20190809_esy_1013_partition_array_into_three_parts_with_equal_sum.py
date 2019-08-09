#-*- coding: utf-8 -*-
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        status = -1
        if len(A) <= 2: return False
        for i in range(len(A)-1):
            diff = A[i+1] - A[i]
            if diff > 0 and status == -1:
                status = 0
            if diff > 0 and status == 0:
                pass
            elif diff < 0 and status == 0:
                status = 1
                # i is peak
            elif diff < 0 and status == 1:
                # going down
                pass
            else:
                return False
        return status == 1


samples = [
    [0, 3, 1, 2],
    [2, 1],
    [3, 5, 5],
    [0, 3, 2, 1],
]
for sample in samples:
    print(Solution().validMountainArray(sample))

