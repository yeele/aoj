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

class Solution_botsu:
    """
    基本的なビット演算のちしきが乏しく
    断念
    """
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        i = 0
        # turn them into 32 bit integer
        a &= (2**33 - 1)
        b &= (2**33 - 1)
        for k in range(32):
            a_ = a & 1
            b_ = b & 1
            if a_ == 1 and b_ == 1:
                if carry == 1:
                    x = 1
                else:
                    x = 0
                carry = 1
            elif a_ == 1 or b_ == 1:
                if carry == 1:
                    x = 0
                    carry = 1
                else:
                    x = 1
                    carry = 0
            else:
                if carry == 1:
                    x = 1
                    carry = 0
                else:
                    x = 0
                    carry = 0
            ans |= (x * 2**i)
            a >>= 1
            b >>= 1
            i += 1
        ans &= (2**33 - 1)
        """
        うん、やっぱり、これで解けてたんだね
        マイナスのコンピューターでの扱いがわかれば直ぐ解けてたね
        if ans > 0xff:
            print("dekai")
            ans = (0xff - (ans & 0xff) + 1) * -1
        else:
            print("chisai")
        """
        return ans


from typing import Tuple
class Solution_botsu2:
    """
    どうやらa >> 1なんかは永遠に1のが左に埋められてダメ！？
    """
    def full_adder(self, a, b, x) -> Tuple[int, int]:
        x = a | b
        c = a & b
        s = x & (~c & 1) # 0の反転は0xffffになっちゃんで。
        return (s, c)

    def getSum(self, a: int, b: int) -> int:
        # a = (a & 2**33-1)
        # b = (b & 2**33-1)
        i = 0
        ans = 0
        c = 0 # initally C is 0
        for i in range(32):
            a_ = a & 1
            b_ = b & 1
            s, c = self.full_adder(a_, b_, c)
            ans = ans | (s << i)
            a >>= 1
            b >>= 1
        return ans


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
        print(bin(ans & 0xff))
        if ans > 0xff:
            print("dekai")
            ans = (0xff - (ans & 0xff) + 1) * -1
        else:
            print("chisai")
        return ans


samples = [
    # 1532pm start
    (1, 2, 3),
    (-2, 3, 1),
    (3, 4, 7),
    (8, 14, 22),
    (-3, -9, -12),
    # 2023pm
    # やっぱりminusのケースでうまくいきません。。。
    # むずかしですね。
    # 11 / 13 test cases passed.

]

# for s, t, expected in samples:
#     ans = Solution().isAnagram(s, t)
#     print(ans)

for a, b, expected in samples:
    #ans = Solution().getSum(a, b)
    ans = Solution_botsu().getSum(a, b)
    print(ans)
