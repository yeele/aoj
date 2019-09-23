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

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = n
        counter = 0
        while x > 0:
            if x & 1 == 1:
                counter += 1
            x >>= 1
        return counter


samples = [
    # 0838am
    (3, 2),
    (4, 1),
    (15, 4),

]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for n, expected in samples:
    ans = Solution().hammingWeight(n)
    print(ans)
