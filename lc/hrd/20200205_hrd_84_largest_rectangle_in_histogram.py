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

class Solution_oop:
    # oops. this is water container solution...
    def largestRectangleArea(self, heights: List[int]) -> int:
        def rect(S):
            i = 0
            if len(S) == 0: return 0
            j = len(S) - 1
            maxi = 0
            while i <= j:
                local = min(S[i], S[j])*(j - i + 1)
                maxi = max(maxi, local)
                if S[i] < S[j]:
                    i += 1
                else:
                    j -= j
            return maxi
        return rect(heights)



class Solution:
    def largestRectangleArea(self, S: List[int]) -> int:
        n = len(S)
        if n == 0: return 0
        dp = [0] * n
        dp[0] = S[0]
        mini = S[0]
        # [2,1,5,6,2,3]
        """
        これまでの最大は？
        左はどこ？高さは？
        """
        left = 0
        height = S[0]
        for i in range(1, n):
            #　S[i]をとるパターン
            area = (i - left + 1) * height
            height = min(height, S[i])
            dp[i] = max(
                dp[i-1],
                dp[]
            )
        return dp[i]





samples = [
    (
        [2,1,5,6,2,3]
    )

]
for S in samples:
    ans = Solution().largestRectangleArea(S)
    print(ans)
