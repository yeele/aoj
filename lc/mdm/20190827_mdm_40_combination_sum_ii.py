#Definition for singly-linked list.
from typing import List
import sys

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
import itertools
class Solution:
    def __init__(self):
        self.ans = []
    def combinationSum2(self, nums: List[int], target: int) -> int:
        self.ans = []
        nums.sort()
        self.rec(nums, target, 0, "")
        # how to remove duplicate from list of list since set doesn't work
        # https://stackoverflow.com/questions/2213923/removing-duplicates-from-a-list-of-lists
        self.ans.sort()
        return list(k for k,_ in itertools.groupby(self.ans))

    def csv_to_list(self, text):
        return [int(x.strip()) for x in text.split(",") if x.strip() is not ""]

    def rec(self, S: List[int], target: int, i, sofar: str):
        logging.debug("rec(%s, %s, %s, %s)" % (S, target, i, sofar))
        length = len(S)
        if target == 0:
            self.ans.append(self.csv_to_list(sofar))
            return
        elif target < 0:
            return
        else:
            if i >= length: return
            x = S[i]
            self.rec(S, target-x, i+1, sofar + "%s,"%x )
            self.rec(S, target, i+1, sofar )







samples = [
    #Î([10,1,2,7,6,1,5], 8, [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ] ),
    ([2,5,2,1,2], 5, [[1,2,2], [5]] ),
]
for nums, k, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum2(nums, k)
    assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (nums, k, ans))
