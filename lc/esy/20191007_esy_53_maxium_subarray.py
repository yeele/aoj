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
    def maxSubArray(self, nums: List[int]) -> int:

        # 今の状況
        # 一個前の状況　
        # で、一個前のが大きければ、それをlocalmaxとしてmaxi 更新、リセット
        # 今の状況のがおおきければ、subarray継続
        # pre = めっちゃ小さいではじめる - sys.maxisize
        # すると一発目はかならず今がおおきくなる。
        # 最後までいったら、今ある状態をsumとする
        # というようなアルゴリズムを6分で考えました
        # 00:00am start implementation
        # 00:18am 25min elapsed...
        # 00:24am failed 187 / 202 test cases passed.
        #

        pre = -sys.maxsize
        i = 0 # left pointer
        total = 0
        maxi = -sys.maxsize
        for j in range(len(nums)):
            curr = nums[j]
            print("i:%s, j:%s, curr:%s, total:%s" % (i, j, curr, total))
            if total + curr > curr:
                print("継続")
                total += curr
                maxi = max(maxi, total)
            elif total + curr < curr:
                print("一回リセットししょ")
                maxi = max(maxi, total)
                total = curr
                maxi = max(maxi, total)
                i = j
            else:
                print("まぁ継続")
                total += curr
                maxi = max(maxi, total)

            pre = curr
        # 最後にもう一回しておく必要がある
        maxi = max(maxi, total)
        return maxi


class Solution_cleaner:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxi = -sys.maxsize
        for j in range(len(nums)):
            curr = nums[j]
            past = total + curr
            if past > curr:
                total += curr
            elif past < curr:
                total = curr
            else:
                total += curr
            maxi = max(maxi, total)

        return maxi







        return 0

samples = [
    #([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([-1], -1),
]


for S, expected in samples:
    ans = Solution().maxSubArray(S)
    print(ans)