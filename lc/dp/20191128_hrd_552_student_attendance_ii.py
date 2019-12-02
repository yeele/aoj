#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

class Solution_my_solution_doesnt_work:
    def checkRecord(self, n: int) -> int:
        cost = [
            0, # P
            0.5, # L
            1, # A
            1.5, # -
        ]
        if n == 0: return 0
        if n == 1: return 3
        if n == 2: return 8
        dp = [[0] * n for _ in range(len(cost))]
        for i in range(n):
            dp[0][i] = 1
        dp[1][0] = 2
        dp[2][0] = 3
        dp[3][0] = 0
        # --- second
        dp[1][1] = 3
        dp[2][1] = 6
        dp[3][1] = 8
        """
        """
        for i in range(1, len(cost)):
            for j in range(2, n):
                # print("_"*20)
                # for row in dp: print(row)
                up = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = up + left

        #for row in dp: print(row)
        return dp[i][j] % (10**9 + 7)


class Solution:
    def checkRecord(self, n: int) -> int:
        """
        dp[i] = OKな(rewardable)レコード数

        dp[0] = 0
        dp[1] = P or A or L いづれも条件満たしている = 3
        dp[2] = 8

        状態として、A２つ以上あったらだめー、Lが三連続したらダメー

        最後がPで、OKな(rewardable)レコード数を保持
        最後がAで、OKな(rewardable)レコード数を保持
        最後がLで、OKな(rewardable)レコード数を保持
        つまり、
        最後の出欠を状態としてもたす。
        すると
        この条件が-> 状態として、A２つ以上あったらだめー、Lが三連続したらダメー
        自ずと、決まってくる。

        n = 2
        PP, LP, AP  =>
        dp[2][P] = 3
        dp[i][P] = dp[i-1][A] + dp[i-1][L] + dp[i-1][P]
        dp[i][A] = dp[i-1][L] + dp[i-1][P]

        dp[i][A] = dp[i-1][A] NG
        dp[i][A] = dp[i-1][P] OK --> ....PA   --> A[i-1]
        dp[i][A] = dp[i-1][L] OK --> ....LA
        dp[i][A] = dp[i-1][L] + dp[i-2][A] NG --> ....ALA
        dp[i][A] = dp[i-1][L] + dp[i-2][P] OK --> ....PLA --> A[i-2]
        dp[i][A] = dp[i-1][L] + dp[i-2][L] OK --> ....LLA
        dp[i][A] = dp[i-1][L] + dp[i-2][L] + dp[i-3][P] OK --> ....PLLA --> A[i-3]



        dp[i][L] = dp[i-1][P] + dp[i-1][A] + dp[i-2][A] + dp[i-2][P]
        """
        if n == 0: return 0
        if n == 1: return 3
        if n == 2: return 8
        dp = [[0] * 3 for _ in range(n+1)]
        #attend = {'A':0, 'L':1, 'P':2}
        A = 0
        L = 1
        P = 2
        dp[1][A] = 1
        dp[1][L]= 1
        dp[1][P] = 1
        dp[2][A] = 2
        dp[2][L]= 3
        dp[2][P] = 3
        dp[3][A] = 4
        dp[3][L]= 7
        dp[3][P] = 8
        mod = 10**9 + 7
        for i in range(4, n+1):
            dp[i][P] = (dp[i-1][A]%mod + dp[i-1][L]%mod + dp[i-1][P]%mod)%mod
            dp[i][A] = (dp[i-1][A]%mod + dp[i-2][A]%mod + dp[i-3][A]%mod)%mod
            dp[i][L] = (dp[i-1][P]%mod + dp[i-1][A]%mod + dp[i-2][P]%mod + dp[i-2][A]%mod)%mod

        #for row in dp: print(row)
        return (dp[n][P]%mod + dp[n][L]%mod + dp[n][A]%mod) % mod


samples = [
    #(2, 8),
    (3, 8),
    (4, 8),
]
for N, expected in samples:
    print("-"*20)
    ans = Solution().checkRecord(N)
    print("(%s) = %s as expected!" % (ans, expected))

