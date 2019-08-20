#Definition for singly-linked list.
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        l = 0
        r = len(height) - 1
        while l < r:
            #print("height[l] -> %s, height[r] -> %s" % (height[l], height[r]))
            cur = (r - l) * min(height[l], height[r])
            #print("r(%s) - l(%s) = %s, so cur is %s" % (r, l, r-l, cur))
            maxi = max(cur, maxi)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxi

samples = [
    [1,8,6,2,5,4,8,3,7]
]
for S in samples:
    ans = Solution().maxArea(S)
    print("%s = %s" % (S, ans))
