#-*- coding: utf-8 -*-
from typing import List


"""
どんな問題か？
1/ （何を問うているのか？）
2/ どんなカテゴリの問題か？
3/ アルゴリズム速度は?
"""

class Solution2:
    def rec(self, num:int):
        ttl = 0
        for s in str(num):
            ttl += int(s)
        return ttl

    def addDigits(self, num: int) -> int:
        ans = self.rec(num)

        while True:
            if ans >= 0 and ans < 10: return ans
            ans = self.rec(ans)




# OK, this is better solution
# not using string...
# https://www.techseries.dev/products/tech-interview-pro/categories/1408104/posts/4821251
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0
            while num > 0:
                sum += (num % 10)
                num = int(num / 10)
            num = sum
        return sum




# 入力Nは徐々というか、十分の一づつ
# 小さくなって行くのでえ
# log(10)N


ans = Solution().addDigits(38)
print(ans)
assert(ans == 2)
