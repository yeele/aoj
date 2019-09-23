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
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = n
        ans = 0
        for i in range(32):
            ans |= ((x & 1) << (31 - i))
            x >>= 1
        return ans




samples = [
    # 1958pm start
    (43261596, 964176192),
    (4294967293, 3221225471),
]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for S, expected in samples:
    ans = Solution().reverseBits(S)
    print(ans)
