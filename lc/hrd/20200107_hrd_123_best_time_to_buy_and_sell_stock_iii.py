#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        NH0 stock持ってない
        H0
        NH1
        H1
        NH2
        """
        if prices is None or len(prices) == 0: return 0
        sz = len(prices)
        maxi = 0
        # logic
        NH0 = 0
        H0 = [-sys.maxsize] * sz
        NH1 = [-sys.maxsize] * sz
        H1 = [-sys.maxsize] * sz
        NH2 = [-sys.maxsize] * sz

        for i in range(0, sz):
            price = prices[i]
            if i == 0: H0[i] = -price
            else: H0[i]  = max(-price, H0[i-1])

            if i >= 1:
                NH1[i] = max( H0[i] + price, NH1[i-1])
            if i >= 2:
                H1[i]  = max(NH1[i] - price, H1[i-1])
            if i >= 3:
                NH2[i] = max( H1[i] + price, NH2[i-1])
        # --- end ---
        # print(" H0 %s" %  H0)
        # print("NH1 %s" % NH1)
        # print("NH2 %s" % NH2)
        return max(0, NH1[i], NH2[i])


samples = [
    ([3,3,5,0,0,3,1,4], 6),
    ([1, 2, 3, 4, 5], 4),
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().maxProfit(S)
    print("(%s) = %s as expected!" % (S, ans))


