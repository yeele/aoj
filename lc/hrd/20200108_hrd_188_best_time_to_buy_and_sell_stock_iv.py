#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        NH0 stock持ってない
        H0
        NH1
        H1
        NH2
        """
        if prices is None or len(prices) == 0: return 0
        if k > len(prices) >> 1: # You got enough transaction times to capture all possible profit
            return sum(prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i])
        sz = len(prices)
        """
        NH[0] = (pre, curr)　とう構成にします。
        NH[1] = ...
        NH[k] = ...
        """
        NH = [0] * (sz + 1)
        maxi = -sys.maxsize
        for i in range(k):
            H = [-sys.maxsize]
            cur_NH= [-sys.maxsize]
            for j in range(sz):
                price = prices[j]
                H.append(max(NH[j] - price, H[-1]))
                cur_NH.append(max(H[j] + price, cur_NH[-1]))
                maxi = max(cur_NH[-1], maxi)
            NH = cur_NH

        return max(0, maxi)


samples = [
    ([3,3,5,0,0,3,1,4], 2, 6),
    ([1, 2, 3, 4, 5], 2, 4),
]
for S, k, expected in samples:
    print("-"*20)
    ans = Solution().maxProfit(k, S)
    print("(%s, %s) = %s as expected!" % (k, S, ans))





