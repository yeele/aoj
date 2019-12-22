#-*- coding: utf-8 -*-
from typing import List
import logging

#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        BF -> O(N^3)
        """
        # https://www.youtube.com/watch?v=5pO2NbB1uJs
        """
        [0,1,2,3,4,5,6,7]
        [1,2,1,2,6,7,5,1], k = 2
               ^   ^   ^
        <--------------   since lexicographically
        """
        c = len(nums) - k # 8 -2 -> 6
        b = c - k # -> 4
        a = b - k
        logging.debug("index:{} {} {}".format(c, b, a))
        logging.debug("k:{} {}".format(k, nums))
        sum_c = sum(nums[c:c+k])
        sum_b = sum(nums[b:b+k])
        sum_a = sum(nums[a:a+k])
        max_c = sum_c
        max_bc = sum_b + max_c
        max_abc = sum_a + max_bc
        logging.debug("sum:{} {} {}".format(sum_c, sum_b, sum_a))
        indice_c = [c]
        indice_bc = [b] + indice_c
        indice_abc = [a] + indice_bc

        while a != 0:
            c -= 1
            b -= 1
            a -= 1
            sum_c += nums[c] - nums[c+k]
            sum_b += nums[b] - nums[b+k]
            sum_a += nums[a] - nums[a+k]
            if sum_c >= max_c:  # equal greater to update in lexicographic order
                max_c = sum_c
                indice_c = [c]
            if sum_b + max_c >= max_bc:
                max_bc = sum_b + max_c
                indice_bc = [b] + indice_c
            if sum_a + max_bc >= max_abc:
                max_abc = sum_a + max_bc
                indice_abc = [a] + indice_bc
        return indice_abc


samples = [
    ([1,2,1,2,6,7,5,1], 2, [0, 3, 5]),
]

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
for S, k ,expected in samples:
    ans = Solution().maxSumOfThreeSubarrays(S, k)
    print(ans)
