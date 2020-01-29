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
    def sol(self, S) -> int:
        print(S)
        N = len(S)
        pre1, pre2, curr, maxi = 0, 0, 0, 0
        for i in range(N): # i:2
            curr = max(pre1, pre2 + S[i]) # curr:4
            maxi = max(maxi, curr)        # maxi:4
            pre2 = pre1                   # pre2:2
            pre1 = curr                   # pre1 4
        return maxi

    def rob(self, S: List[int]) -> int:
        if len(S) == 1: return S[0]
        else:
            return max(
                self.sol(S[1:]),
                self.sol(S[:-1])
            )

samples = [
    ([2, 3, 2], 3)
]
for S, expected in samples:
    ans = Solution().rob(S)
    print(ans)
