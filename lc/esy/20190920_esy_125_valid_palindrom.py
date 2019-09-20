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



samples = [
    ( "A man, a plan, a canal: Panama", True),
    ("race a car", False),
    # 0902am
    ("OP", False),
    ("0P", False), # this is very hard to see

    # 問題文のこれ、alphanumeric characters
    # 英数字という意味で
    # 数字もふくみます！！！がびーん
]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for s, expected in samples:
    ans = Solution().isPalindrome(s)
    print(ans)
