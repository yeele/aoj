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

# https://leetcode.com/problems/delete-and-earn/discuss/479017/Simple-Python-DP
# ヒントにしたし
# https://leetcode.com/problems/delete-and-earn/solution/
# もみたけど、方向はよくて、ヒントをみて自力でclearした。
# 特に、バグがちゃんとみつけれてよかった。
# バグはここにあった！dp[i-1]もわすれてはいけない！
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 0: return 0
        dp = [0] * (n+1)
        dp[0] = 0
        if n == 0: return dp[0]
        dp[1] = 1
        if n == 1: return dp[1]
        dp[2] = 2
        if n == 2: return dp[2]
        dp[3] = 5
        if n == 3: return dp[3]
        for i in range(4, n+1):
            dp[i] = dp[i-1]*2 + dp[i-2]*0  + dp[i-3]*1
            #dp[i] = dp[i-1]*0 + dp[i-2]*2  + dp[i-3]*1
            #dp[i] = dp[i-1] + dp[i-2]*2  + dp[i-3]*2
            # https://leetcode.com/problems/domino-and-tromino-tiling/discuss/407367/Python-O(0)-space
            #dp[i] = dp[i-1] + dp[i-2]*2  + dp[i-3]*5
            #dp[i] = dp[i-1] + dp[i-2]*2  + dp[i-3]*2

        return dp[n]


#https://leetcode.com/problems/domino-and-tromino-tiling/discuss/406649/Python-DP-half-and-full
#分かりやすい

#https://leetcode.com/problems/domino-and-tromino-tiling/discuss/182594/Python-1-liner-O(log-n)-time-O(1)-space-with-explanation
#わかりやすいけど、
#すごいけど、わからない。


samples = [
      (0, 1),
    (1, 1),
    (2, 2),
    (3, 5),
    (4, 11),
    (5, 25),

]
for n, ex in samples:
    ans = Solution().numTilings(n)
    print(ans)
