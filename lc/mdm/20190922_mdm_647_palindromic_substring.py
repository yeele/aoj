#-*- coding: utf-8 -*-
from typing import List
import math

import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped


class Solution:
    def get_palindrome(self, S: str, i: int, j: int) -> bool:
        # i is starting index
        length = len(S)
        ans = 0
        while i >= 0 and j < length:
            if S[i] == S[j]:
                #ans = S[i:j+1]
                ans += 1
            else:
                break
            i -= 1
            j += 1
        return ans

    def countSubstrings(self, s: str) -> int:
        if s == "": return ""
        length = len(s)
        ans = 0
        for i in range(length):
            palindrome = self.get_palindrome(s, i, i)
            ans += palindrome
            palindrome = self.get_palindrome(s, i, i+1)
            ans += palindrome
        return ans


samples = [
    # 1515pm start
    ( "abc", 3),
    ("aaa", 6),
    # 1520pm done !
]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for s, expected in samples:
    ans = Solution().longestPalindrome(s)
    print(ans)
