#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

class Solution_first_solution_1hour_to_implement:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        sz1 = len(s1)
        sz2 = len(s2)
        sz3 = len(s3)
        if (sz1 + sz2) != sz3: return False
        if sz3 == 0: return False

        dp = [[False]*(sz1+1) for _ in range(sz2+1)]

        # fill columns
        for j in range(sz1+1):
            if j > 0:
                _j = j - 1
                left = dp[0][_j]
                at = left.find(s1[_j])
                if at >= 0: # found
                    dp[0][j] = left[0:at] + left[at+1:] # remove the char
            else:
                dp[0][j] = s3

        # fill rows
        for i in range(sz2+1):
            if i > 0:
                _i = i - 1
                left = dp[_i][0]
                at = left.find(s2[_i])
                if at >= 0: # found
                    #dp[j] = True
                    dp[i][0] = left[0:at] + left[at+1:] # remove the char
            else:
                dp[i][0] = s3

        # main
        for i in range(1, sz2+1):
            for j in range(1, sz1+1):
                _i = i - 1
                _j = j - 1
                for row in dp: print(row)

                left = dp[i][_j]
                if left == False: return False

                at = left.find(s1[_j])
                if at >= 0: # found
                    dp[i][j] = left[0:at] + left[at+1:] # remove the char
                else: return False

        for row in dp: print(row)
        return True



class Solution_wrong:
    """
    by implementing first logic; Solution_first_solution_1hour_to_implement
    I realized that
    it may be as simple as
    just removing all characters s1 from s3.
    then, try removing all character s2 from the left. then each char on s2 must be at always
    at 1st index of left.

    ...

    implemented in 5 mins, but failed... this doesn't work like this way.
    cuz, you can't alway delete first found index in round of s1....
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        sz1 = len(s1)
        sz2 = len(s2)
        sz3 = len(s3)
        if (sz1 + sz2) != sz3: return False
        if sz3 == 0: return False

        left = s3
        print("initial left {}".format(left))
        for c in s1:
            at = left.find(c)
            if at == -1: return False
            left = left[0:at] + left[at+1:]

        print("after s1 processed, left {}".format(left))
        for c in s2:
            at = left.find(c)
            if at != 0: return False # must be 1st index!!!!
            left = left[0:at] + left[at+1:]

        print("finally left {}".format(left))
        return True

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        sz1 = len(s1)
        sz2 = len(s2)
        sz3 = len(s3)
        if (sz1 + sz2) != sz3: return False
        if sz3 == 0: return False

        dp = [[False]*(sz1+1) for _ in range(sz2+1)]

        # fill columns
        for j in range(sz1+1):
            if j > 0:
                _j = j - 1
                left = dp[0][_j]
                at = left.find(s1[_j])
                if at >= 0: # found
                    dp[0][j] = left[0:at] + left[at+1:] # remove the char
            else:
                dp[0][j] = s3

        # fill rows
        for i in range(sz2+1):
            if i > 0:
                _i = i - 1
                left = dp[_i][0]
                at = left.find(s2[_i])
                if at >= 0: # found
                    #dp[j] = True
                    dp[i][0] = left[0:at] + left[at+1:] # remove the char
            else:
                dp[i][0] = s3

        # main
        for i in range(1, sz2+1):
            for j in range(1, sz1+1):
                _i = i - 1
                _j = j - 1
                for row in dp: print(row)

                left = dp[i][_j]
                if left == False: return False

                at = left.find(s1[_j])
                if at >= 0: # found
                    dp[i][j] = left[0:at] + left[at+1:] # remove the char
                else: return False

        for row in dp: print(row)
        return True

samples = [
    #("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    # ("", "", "a", False),
    # 89 / 101 test cases passed.
    # https://leetcode.com/submissions/detail/280064502/
    # by TLE
]
for S1, S2, S3, expected in samples:
    print("-"*20)
    ans = Solution().isInterleave(S1, S2, S3)
    print("(%s) = %s as expected!" % (ans, expected))

