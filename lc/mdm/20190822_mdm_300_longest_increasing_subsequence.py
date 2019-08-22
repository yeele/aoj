#Definition for singly-linked list.
from typing import List
import sys

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0: return 0
        sz = len(nums)
        L = [0] * sz
        for i in range(sz):
            if i == 0:
                L[0] = 1
                logging.debug("%s:initially" % L)
                continue
            maxi = -1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    maxi = max(L[j], maxi)
            if maxi != -1:
                # found
                L[i] = maxi + 1
            else:
                #L[i] = L[i-1]
                L[i] = 1
            logging.debug("%s" % L)

        return max(L)



samples = [
    # ([10,9,2,5,3,7,101,18], 4),
    # ([4,10,4,3,8,9], 3),
    ([1,3,6,7,9,4,10,5,6], 6)
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().lengthOfLIS(S)
    assert ans == expected, "%s should be %s but %s" % (S, expected, ans)
    print("%s = %s as expected!" % (S, ans))
