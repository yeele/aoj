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
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if n == 1: return 0
        dp = [0] * n
        swap = 0
        for i in range(0, n):
            if i > 0:
                if not A[i-1] < A[i] or not B[i-1] < B[i]:
                    A[i], B[i] = B[i], A[i]
                    swap += 1
            if i < n - 1:
                if not A[i] < A[i+1] or not B[i] < B[i+1]:
                    A[i+1], B[i+1] = B[i+1], A[i+1]
                    swap += 1
        #print(A)
        #print(B)
        return swap


#https://leetcode.com/problems/domino-and-tromino-tiling/discuss/406649/Python-DP-half-and-full
#分かりやすい

#https://leetcode.com/problems/domino-and-tromino-tiling/discuss/182594/Python-1-liner-O(log-n)-time-O(1)-space-with-explanation
#わかりやすいけど、
#すごいけど、わからない。

samples = [
    # (
    #     [1,3,5,4],
    #     [1,2,3,7],
    #     1
    # ),
    (
        [0,4,4,5,9],
        [0,1,6,8,10],
        1
    )

]
for A, B, e in samples:
    ans = Solution().minSwap(A, B)
    print(ans)
