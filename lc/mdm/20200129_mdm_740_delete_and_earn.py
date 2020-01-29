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
    def deleteAndEarn(self, nums: List[int]) -> int:
        def f(x): # return maximum point at 1
            pass
        memo = defaultdict(int)
        for x in nums:
            memo[x] += 1
        memo = { k: k*v for k, v in memo.items() }
        print(memo)
        N = 10001
        maxi = 0
        # number of values limited to 1 to 10000
        dp = [0] * N
        for i in range(N):
            if i - 2 >= 0:
                #dp[i] = dp[i-2] + memo.get(i, 0)  # バグはここにあった！dp[i-1]もわすれてはいけない！
                dp[i] = max(dp[i-2] + memo.get(i, 0), dp[i-1])
            else:
                dp[i] = memo.get(i, 0)
            maxi = max(maxi, dp[i])
        return maxi



samples = [
      #([3, 4, 2] 6),
    ([2, 2, 3, 3, 3, 4], 9),
]
for S, expected in samples:
    ans = Solution().deleteAndEarn(S)
    print(ans)
