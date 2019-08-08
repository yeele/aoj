#-*- coding: utf-8 -*-
from typing import List
import math


class Solution:
    def is_parandrome(self, s):
        half_idx = math.ceil(len(s)/2)
        j = len(s)-1
        i = 0
        while i <= j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        #print("is_parandrome(%s) == yes" % s)
        return True

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        ret = s[0]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                #print (i, j)
                y = self.is_parandrome(s[i:j+1])
                ret = s[i:j+1] if y and len(s[i:j+1]) > len(ret) else ret
        return ret




#print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("ac"))
