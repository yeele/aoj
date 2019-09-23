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




from typing import Tuple
class Solution:
    def half_adder(self, a, b) -> Tuple[int, int]:
        s = 1 & (a ^ b)
        c = 1 & (a & b)
        return (s, c)

    def full_adder(self, a, b, x) -> Tuple[int, int]:
        (s1, c1) = self.half_adder(a, b)
        (s, c2) = self.half_adder(s1, x)
        c = (c1 | c2)
        return (s, c)

    def getSum(self, a: int, b: int) -> int:
        # a = (a & 2**33-1)
        # b = (b & 2**33-1)
        i = 0
        ans = 0
        c = 0 # initally C is 0
        for i in range(32):
            a_ = (a >> i) & 1
            b_ = (b >> i) & 1
            s, c = self.full_adder(a_, b_, c)
            ans = ans | (s << i)
        #print(bin(ans & 0xff))
        if ans > 0xff:
            #print("dekai")
            ans = (0xff - (ans & 0xff) + 1) * -1
        else:
            #print("chisai")
            pass
        return ans

    def getNCarry(self, a: int, b: int) -> int:
        i = 0
        ans = 0
        c = 0 # initally C is 0
        number_of_carryover = 0
        for i in range(32):
            a_ = (a >> i) & 1
            b_ = (b >> i) & 1
            s, c = self.full_adder(a_, b_, c)
            number_of_carryover += c
            ans = ans | (s << i)
        #print(bin(ans & 0xff))
        if ans > 0xff:
            #print("dekai")
            ans = (0xff - (ans & 0xff) + 1) * -1
        else:
            #print("chisai")
            pass
        return number_of_carryover

    def countBits(self, num: int) -> List[int]:
        counter = 0
        j = 1 # 桁が増えたかどうかの判定用
        p = 0
        ans = []
        for i in range(0, num+1):
            if i == 0:
                ans.append(0)
            else:
                keta = 2**j
                if i == keta:
                    j += 1
                    counter = 1
                else:
                    if i & 1 == 1: # ０から1へ、第一位がなった時
                        counter += 1
                    number_of_carryover = self.getNCarry(p, 1)
                    if number_of_carryover >= 2:
                        counter -= (number_of_carryover-1)

                ans.append(counter)
            p = i
        return ans


samples = [
    # 0915am
    (2, [0, 1, 1]),
    (5, [0,1,1,2,1,2]),
    (8, []),
]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for n, expected in samples:
    ans = Solution().countBits(n)
    print(ans)
