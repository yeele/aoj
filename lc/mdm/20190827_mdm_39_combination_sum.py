#Definition for singly-linked list.
from typing import List
import sys

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def __init__(self):
        self.ans = []
    def combinationSum(self, nums: List[int], target: int) -> int:
        self.ans = []
        self.rec(nums, target, 0, "")
        return self.ans
    def csv_to_list(self, text):
        return [int(x.strip()) for x in text.split(",") if x.strip() is not ""]

    def rec(self, S: List[int], target: int, i, sofar: str):
        logging.debug("rec(%s, %s, %s, %s)" % (S, target, i, sofar))
        length = len(S)
        if i >= length: return
        x = S[i]
        if target == 0:
            self.ans.append(self.csv_to_list(sofar))
            return
        elif target < 0:
            return
        else:
            self.rec(S, target-x, i, sofar + "%s,"%x )
            self.rec(S, target, i+1, sofar )







samples = [
    ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
]
for nums, k, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum(nums, k)
    assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (nums, k, ans))
