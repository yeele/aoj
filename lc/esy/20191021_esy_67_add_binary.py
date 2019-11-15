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

import sys
sys.setrecursionlimit(314159265)
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def binary_to_int(characters: str):
            ans = 0
            sz = len(characters)
            for i in range(sz-1, -1, -1):
                c = characters[i]
                j = (sz-1-i)
                if c == "1":
                    ans += 2**j
            return ans
        def int_to_binary(x: int):
            stack = []
            if x == 0: return "0"
            while x:
                if x & 1:
                    stack.append("1")
                else:
                    stack.append("0")
                x >>= 1
            ans = ""
            while stack:
                y = stack.pop()
                ans += y
            return ans

        a_int = binary_to_int(a)
        b_int = binary_to_int(b)
        y_int = a_int + b_int

        return int_to_binary(y_int)

samples = [
    # ("11","1", "100"),
    # ("1010", "1011", "10101"),
    ("0", "0", "0"),
]


for a, b, expected in samples:
    ans = Solution().addBinary(a, b)
    print(ans)