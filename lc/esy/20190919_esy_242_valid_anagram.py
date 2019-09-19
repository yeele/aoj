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

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        if length != len(t): return False
        ZERO = defaultdict(int)
        for i in range(length):
            ZERO[s[i]] += 1
            ZERO[t[i]] -= 1
        for c, n in ZERO.items():
            if n != 0:
                return False
        return True

samples = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    #文字列が0サイズだったら、Trueとしていいですか？ （こういう質問前もっていうの大事)good job!
    ("", "", True),
]

for s, t, expected in samples:
    ans = Solution().isAnagram(s, t)
    print(ans)


