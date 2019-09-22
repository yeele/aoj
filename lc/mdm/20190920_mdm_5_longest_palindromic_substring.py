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
        ans = ""
        while i >= 0 and j < length:
            if S[i] == S[j]:
                ans = S[i:j+1]
            else:
                break
            i -= 1
            j += 1
        return ans

    def longestPalindrome(self, s):
        if s == "": return ""
        length = len(s)
        longest = ""
        for i in range(length):
            palindrome = self.get_palindrome(s, i, i)
            if len(palindrome) > len(longest):
                longest = palindrome
            palindrome = self.get_palindrome(s, i, i+1)
            if len(palindrome) > len(longest):
                longest = palindrome
        return longest


class Solution_tle:
    def isPalindrome(self, s: str) -> bool:
        # l, r point
        # ignore non-alphabet
        # case insensitive
        length = len(s)
        if s == None: return False
        if s == "": return True

        l = 0
        r = length-1

        while l <= r:
            if not (s[l].isalpha() or s[l].isnumeric()) : l+=1; continue;
            if not (s[r].isalpha() or s[r].isnumeric()): r-=1; continue;
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True

    def longestPalindrome(self, s):
        if s == "": return ""
        length = len(s)
        longest = ""
        for i in range(length):
            for j in range(i, length):
                if self.isPalindrome(s[i:j+1]):
                    if len(s[i:j+1]) > len(longest):
                        longest = s[i:j+1]
        return longest



samples = [
    # 0935am start
    ( "babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    # 1015am TLE
    # 89 / 103 test cases passed.
    # この問題に関しては成長してない、私のシナプスが。
    # 今回で克服したい。
    # O(N^3) -> O(N^2)にもっていけないか？
]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for s, expected in samples:
    ans = Solution().longestPalindrome(s)
    print(ans)
