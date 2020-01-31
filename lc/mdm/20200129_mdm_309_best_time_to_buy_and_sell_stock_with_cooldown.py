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

from collections import defaultdict
class Solution:
    # https://kennyzhuang.gitbooks.io/algorithms-collection/content/buy_and_sell_stock_with_cooldown.html
    def maxProfit(self, S: List[int]) -> int:
        if S is None: return 0
        n = len(S)
        if n <= 1: return 0
        buy = [0] * (n+1)
        sell = [0] * (n+1)
        buy[0] = -S[0]
        sell[0] = 0
        for i in range(1, n):
            sell[i] = max(sell[i-1], buy[i-1] + S[i])
            buy[i]  = max(buy[i-1], sell[i-2] - S[i])
        return sell[n-1]



samples = [
    ([1, 2, 3, 0, 2])
]
for S in samples:
    ans = Solution().maxProfit(S)
    print(ans)
