


#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3): return False
        route = [ [0] * (len(s1)+1) for _ in range(len(s2)+1)]
        def print_route():
            for row in route:
                print(row)
        #print_route()

        def valid(i, j, di):
            if (j < 1 or j > len(s1)) and di == "right": return False
            if (i < 1 or i > len(s2)) and di == "bottom": return False
            return True
        def get_route(i, j, di="right"):
            if valid(i, j, di):
                if di == "right":
                    return s1[j-1]
                elif di == "bottom":
                    return s2[i-1]
                else:
                    assert('not supported di %s' % di)
            return None
        def ppri_s1(j):
            print(' ' + s1)
            print( (' ' * (j) if j > 0 else '') + '^')
        def ppri_s2(i):
            print(' ' + s2)
            print( (' ' * (i) if i > 0 else '') + '^')
        def ppri_s3(k):
            print(s3)
            print( (' ' * (k) if k > 0 else '') + '^')
        def ppri(i, j, k):
            print("i = %s, j = %s, k = %s" % (i, j, k))
            ppri_s1(j)
            ppri_s2(i)
            if k >= 0:
                ppri_s3(k)
            print('_'*16, end='')


        def crawl(i, j, k):
            if i == len(s2) and j == len(s1):
                #print("ret : %s" % True)
                return True
            else:
                #ppri(i, j, k)
                if k == -1: c = s3[0]
                else: c = s3[k+1]
                s1c = get_route(i, j+1, "right")
                if s1c == c:
                    ret1 =  crawl(i, j+1, k+1)
                else:
                    ret1 = False
                s2c = get_route(i+1, j, "bottom")
                if s2c == c:
                    ret2 = crawl(i+1, j, k+1)
                else:
                    ret2 = False
                ret = any([ret1, ret2])
                #print("ret : %s" % ret)
                if any([ret1, ret2]):
                    return True
                else:
                    return False

        # print(get_route(len(s2), len(s1), "right"))
        # print(get_route(len(s2), len(s1), "bottom"))
        ret1 = crawl(0, 0, -1) # s1の一文字めをスタートとする場合
        return ret1




samples = [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "a", False),
    # 89 / 101 test cases passed.
    # https://leetcode.com/submissions/detail/280064502/
    # by TLE
]
for S1, S2, S3, expected in samples:
    print("-"*20)
    ans = Solution().isInterleave(S1, S2, S3)
    print("(%s) = %s as expected!" % (ans, expected))

