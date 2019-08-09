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

from functools import reduce
class Solution_division:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        product = reduce(lambda x, y : x * y, nums)
        for i, n in enumerate(nums):
            ret.append(product/n)
        return ret


from functools import reduce
class Solution_timeexceeded:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        cache_forward = []
        cache_backward = []
        for i, n in enumerate(nums):
            if i == 0:
                cache_forward.append(1)
            else:
                cache_forward.append(reduce(lambda x, y : x * y, nums[0:i]))

        for i, n in enumerate(nums):
            if i == len(nums)-1:
                cache_backward.append(1)
            else:
                cache_backward.append(reduce(lambda x, y : x * y, nums[i+1:]))

        logging.debug("cache_forward:%s" % cache_forward)
        logging.debug("cache_backward:%s" % cache_backward)

        return list(map(lambda t: t[0]*t[1], list(zip(cache_forward, cache_backward))))



from functools import reduce
class Solution_timeexceeded_again_offcourse_nothing_changed:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        length = len(nums)
        for i in range(length):
            forward = 1
            backward = 1
            if i == 0:
                forward = 1
            else:
                forward = reduce(lambda x, y : x * y, nums[0:i])
            if i == length-1:
                backward = 1
            else:
                backward = reduce(lambda x, y : x * y, nums[i+1:])
            ret.append(forward*backward)
        return ret



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        length = len(nums)
        product_forward = []
        product_backward = []
        product = 1

        for i in range(length):
            if i == 0:
                product *= 1
                product_forward.append(product)
            else:
                product *= nums[i-1]
                product_forward.append(product)

        product = 1
        for i in range(length-1, -1, -1):
            if i == length-1:
                product *= 1
                product_backward.insert(0, product)
            else:
                product *= nums[i+1]
                product_backward.insert(0, product)

        # print(product_forward)
        # print(product_backward)
        return list(map(lambda t: t[0]*t[1], zip(product_forward, product_backward)))



import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
"""
1002am 
Input:  [1,2,3,4]
Output: [24,12,8,6]

[2, 7, 1]
[7, 2, 14]

1017am watch answer video cuz, I didn't come with the solution.

so, 

make precomputation by
calculating product upto i element in forward direction and backward direction

in the case of [1, 2, 3, 4]

cache_forward = [
1,
1,
2,
6
]
cache_backward = [
24,
12,
4,
1

]

1020am coding start
1030am coding done

but time exceeded


1053am accepted



"""

samples = [
    [1, 2, 3, 4],
    [2, 7, 1]
]

for nums in samples:
    ans = Solution().productExceptSelf(nums)
    print(ans)