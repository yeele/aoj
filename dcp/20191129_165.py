#-*- coding: utf-8 -*-
from typing import List
import sys
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

import heapq
class Solution_fuckedup:
    def solve(self, S):
        heaplist = []
        indice = {}
        if S is None or len(S) == 0: return S
        ans = [0] * len(S)
        for i, n in enumerate(S):
           indice[n] = i
           heapq.heappush(heaplist, n)
        print("indices : {}".format(indice))
        print("heaplist : {}".format(heaplist))

        for i in range(len(S)):
            n = heapq.heappop(heaplist)
            idx = indice[n]
            #右から何番目？
            ridx = len(S)-1 - idx
            # 右から何番目、と　数字が何番目い小さいか？
            # で、自分の右に何人いるかがわからないか？
            # 3, 4, 9, 6, 1
            #
            ans[indice[n]] = ridx - i

        return ans


class Solution:
    def solve(self, S):
        value_index = []
        if S is None or len(S) == 0: return S
        ans = [0] * len(S)
        for i, n in enumerate(S):
            value_index.append((n, i))

        value_index_by_value = sorted(value_index, key=lambda tp : tp[0])
        value_index_by_index = sorted(value_index, key=lambda tp : tp[1])

        print("value_index_by_value {}".format(value_index_by_value))
        print("value_index_by_index {}".format(value_index_by_index))

        for n, i in value_index_by_value:
            for j in range(0, i):
                m = value_index_by_index[j][0]
                k = value_index_by_index[j][1]
                if m > n:
                    ans[k] += 1
        """
        indexmap = [3:0, 4:1, 9:2, 6:3, 1:4]
        3, 4, 9, 6, 1
        indexmap.sort()
        [1:4, 3:0, 4:1, 6:3, 9:2] # 値順
        [3:0, 4:1, 9:2, 6:3, 1:4] # index順
        
        1:4, 4以前のindex && 値>1 に +1         ---> [3:0:1, 4:1:1, 9:2:1, 6:3:1, 1:4:0]
        3:0  0以前のindex && 値>3 に +1 でもない。--> [3:0:1, 4:1:1, 9:2:1, 6:3:1, 1:4:0]
        4:1  1以前のindex && 値>4 に +1          --> [3:0:1, 4:1:1, 9:2:1, 6:3:1, 1:4:0]  (3>4　不成立）
        6:3  3以前のindex && 値>6 に +1          --> [3:0:1, 4:1:1, 9:2:2, 6:3:1, 1:4:0]  (9>6のみ成立）
        9:2  2以前のindex && 値>9 に +1          --> [3:0:1, 4:1:1, 9:2:2, 6:3:1, 1:4:0]  (N>9なので不成立）
        
        ということで答えは
        --> [3:0:1, 4:1:1, 9:2:2, 6:3:1, 1:4:0] 
        [1, 1, 2, 1, 0]
        と正解。tO(N) + tO(NlogN) + O(N * N/2)
        ...
        時間がだいぶたったのでこれで実装します。
        
        
        
        この考えはダメだった。燃えるゴミ。
        indexmap = [3:0, 4:1, 9:2, 6:3, 1:4]
        indexmap.sort()
        [1:4, 3:0, 4:1, 6:3, 9:2]
        [1, 1, 2, 1, 0]
        
        3, 4, 9, 6, 1
        1, 3, 4, 6, 9
        0, 1, 1, 2, 1
        1, 1, 2, 1, 0
        """



        return ans



samples = [
    (
        [3, 4, 9, 6, 1],
        [1, 1, 2, 1, 0]
    )
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().solve(S)
    print("(%s) = %s as expected!" % (ans, expected))

