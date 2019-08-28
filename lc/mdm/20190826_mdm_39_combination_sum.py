#Definition for singly-linked list.
from typing import List
import sys

import logging
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
import sys
sys.setrecursionlimit(1000000)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.rec(candidates, 0, [], 0, target)

    def rec(self, S: List[int], i, comb, total, target) -> List[List[int]]:
        length = len(S)
        print("i:%s, length:%s" % (i, length))
        if i >= length: return []
        for j in range(length):
            print("i:%s, j:%s" % (i, j))
            if j < i: continue
            x = S[j]
            comb4 = comb[:]
            comb5 = comb[:]
            comb.append(x)
            comb1 = comb[:]
            comb2 = comb[:]
            comb3 = comb[:]

            total += x
            if total == target:
                return [comb1]
            elif total > target:
                return []
            else:
                tmp = []
                tmp += self.rec(S, i, comb2, total, target)
                tmp += self.rec(S, i+1, comb3, total, target)
                tmp += self.rec(S, i, comb4, total-x, target)
                tmp += self.rec(S, i+1, comb5, total-x, target)
                return tmp


samples = [
    ([2,3,6,7], 7, [[7], [2, 2, 3]]),
]
for nums, k, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum(nums, k)
    assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (nums, k, ans))
