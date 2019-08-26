#Definition for singly-linked list.
from typing import List
import sys

import logging
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        length = len(nums)
        dp = [ [[]] * length for _ in range(length) ]
        def print_dp():
            for row in dp:
                logging.debug(row)
        def valid_dp(i, j):
            if i < 0 or i >= length: return False
            if j < 0 or j >= length: return False
            return True
        def get_dp(i, j, default=[]):
            if valid_dp(i, j): return dp[i][j]
            else: return default
        def set_dp(i, j, value):
            if value and valid_dp(i, j):
                dp[i][j] = value

        for i in range(length):
            for j in range(length):
                new_combs = []
                pre_combs = get_dp(i, j, [])
                X = nums[i]
                Y = j
                # これまでのコンビ
                for comb in pre_combs:
                    new_combs.append(comb.append(X))
                    new_combs.append(comb.insert(0, X))
                if not valid_dp(i, j-X) and Y % X == 0:
                    new_combs.append([X])
                print(new_combs)
                set_dp(i, j,
                    [ list(x) for x in list(set([tuple(x) for x in new_combs])) ]
                )

        print_dp()
        return len(get_dp(i, j))


samples = [
    ([1, 2, 3], 4, 7),
]
for nums, k, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum4(nums, k)
    assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (nums, k, ans))
