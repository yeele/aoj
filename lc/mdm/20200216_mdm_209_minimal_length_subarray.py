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
    def minSubArrayLen(self, x: int, S: List[int]) -> int:

        if S is None: return 0
        N = len(S)
        if N == 0: return 0

        def sum(i, j):
            ans = 0
            for k in range(i, j+1):
                ans += S[k]
            return ans

        i, j= 0, 0
        mini = sys.maxsize
        """
                    i
        2 3 1 2 4 3
                    j
        G = 4
        """
        while True:
            local = sum(i, j)
            print(i, j, local, N-1)

            if local == x:
                mini = min(mini, j-i+1)
                if i == N-1 and j == N-1:
                    print("miso")
                    break
                if j == N-1:
                    i += 1
                else:
                    j += 1
            elif local > x:
                mini = min(mini, j-i+1)
                if i == N-1 and j == N-1:
                    print("soup")
                    break
                i += 1
            else:
                if i == N-1 and j == N-1:
                    print("miso-soup")
                    break
                if j == N-1:
                    i += 1
                else:
                    j += 1

            if j == N:
                j = N - 1
        return mini




samples = [
    (
        [2,3,1,2,4,3],
         7
    ),
    (
        [1,2,3,4,5], 11
    )



]
for S, x in samples:
    ans = Solution().minSubArrayLen(x, S)
    print(ans)
