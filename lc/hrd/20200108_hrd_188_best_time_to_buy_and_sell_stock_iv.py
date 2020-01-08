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
        sz = len(prices)
        """
        NH[0] = (pre, curr)　とう構成にします。
        NH[1] = ...
        NH[k] = ...
        """
        #NH = [[-sys.maxsize, -sys.maxsize]] * (k+1) # unintended reference
        NH = []
        # for _ in range(k*2+1):
        #     NH.append([-sys.maxsize, -sys.maxsize]) # Memory Exceeded.
        NH[0] = [0, 0]
        NH[1] = [-sys.maxsize, -sys.maxsize]
        for i in range(0, sz):
            price = prices[i]
            for j in range(1, k*2+1):
                if j % 2 == 0:
                    NH[j][0] = max(NH[j-1][0] + price, NH[j][1])
                else:
                    NH[j][0] = max(NH[j-1][0] - price, NH[j][1])
                NH[j][1] = NH[j][0]

        for i, (cur, pre) in enumerate(NH):
            print(" HH[%s] = (%s, %s)" %  (i, cur, pre))
        return max(0, max(cur for cur, pre in NH))


samples = [
    ([3,3,5,0,0,3,1,4], 2, 6),
    ([1, 2, 3, 4, 5], 2, 4),
]
for S, k, expected in samples:
    print("-"*20)
    ans = Solution().maxProfit(k, S)
    print("(%s, %s) = %s as expected!" % (k, S, ans))





