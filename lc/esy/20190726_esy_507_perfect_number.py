#-*- coding: utf-8 -*-
from typing import List

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ttl = 0
        for i in range(1, num):
            if num % i == 0:
                ttl += i
                if ttl > num:
                    return False
        return ttl == num


    def naive(self, num: int) -> bool:
        divs = []
        for i in range(1, num):
            if num % i == 0:
                divs.append(i)
        #print(divs)
        #print(sum(divs))
        return sum(divs) == num


ans = Solution().checkPerfectNumber(28)
print(ans)
