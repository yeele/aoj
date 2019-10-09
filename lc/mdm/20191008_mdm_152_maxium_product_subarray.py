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

class Solution_wrong:
    def maxProduct(self, nums: List[int]) -> int:
        minuss = 0
        sofar = 1
        local_sofar = 0
        maxi = -sys.maxsize
        for i in range(len(nums)):
            print (nums[i])

            x = nums[i]
            if x < 0:
                minuss += 1
                if minuss % 2 == 0: # even
                    local_sofar = sofar * x
                else: # odd
                    local_sofar = x
            else:
                local_sofar = x if local_sofar <= 0 else local_sofar * x
            sofar *= x
            maxi = max(maxi, local_sofar)

        return maxi


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sofar = 1
        maxi = -sys.maxsize
        n = len(nums)
        P = []
        signs = []
        minuss = 0
        zeroi = []
        for i in range(n):
            x = nums[i]
            if x == 0:
                zeroi.append(i)
            else:
                if i > 0:
                    zeroi.append(zeroi[i-1])
                else:
                    zeroi.append(-1)

            if i > 0 and x == 0:
                sofar = P[i-1] if sofar != 0 else x
            else:
                if i > 0:
                    sofar = sofar * x if nums[i-1] != 0 else x
                else:
                    sofar = x
            P.append(sofar)
            if x < 0:
                minuss += 1
            signs.append(minuss)
        print(nums)
        print(P)
        print(signs)
        print(zeroi)
        minuss = 0

        for i in range(len(nums)):
            x = nums[i]
            tracing_point = n-1
            #最寄りの0を探す旅
            while tracing_point >= 0 and zeroi[tracing_point] and zeroi[tracing_point] > i:
                tracing_point = zeroi[tracing_point]
                if tracing_point > 0:
                    if zeroi[tracing_point-1] >= 0 and zeroi[tracing_point-1] > i:
                        tracing_point = zeroi[tracing_point-1]
                    else:
                        break
                else:
                    break
            tp = tracing_point
            #print("tp:%s. In passing n-1:%s" % (tracing_point, n-1))
            if x < 0:
                minuss += 1
                if minuss % 2 == 0:
                    maxi = max(maxi, P[i], nums[i])
                z = (signs[tp] - signs[i])
                sign = -1 if z % 2 == 1 else 1
                if i == 0 and n == 1:
                    maxi = max(maxi, P[i], nums[i])
                else:
                    if i == tp:
                        maxi = max(maxi, nums[i])
                    else:
                        if P[tp] == P[i] and nums[tp] == 0:
                            maxi = max(maxi, 0); continue
                        y = sign*abs(P[tp]//(1 if P[i]==0 else P[i]))
                        if nums[i] == 0:
                            maxi = max(maxi, P[tp])
                        maxi = max(maxi, y, P[i], nums[i])
            else:
                if nums[i] == 0:
                    maxi = max(maxi, P[tp])
                maxi = max(maxi, P[i], nums[i])
        return maxi




# 7mins to think
# 00:10 am start implementing
# 00:28 am sample case passed
samples = [
    ([2,3,-2,4], 6),
    ([-2,0,-1], 0),
    # # # 00:28 am failed at 145 / 184 test cases passed
    ([2,-5,-2,-4,3], 24),
    # 累積サムでひらめいた
    # 00:37am
    # 00:47 implemented, above 3 cases passed
    ([-2], -2),
    # 00:50 fixed 2/184 failed test cae
    # 00:51 fixed 4/184 failed test cae
    ([2], 2),
    ([-4,-3], 12),
    ([0, 2], 2),
    # next mornaing resumed.
    # fixed above by resetting sofar when last sofar is 0
    # 0935am failed at 160 / 184 test cases passed.
    # now, passed 160 so more confident with this algorithm
    ([3,-1,4], 4),
    # 1008am implemented... take too long
    # 168 / 184 test cases passed.
    ([-1,-2,-3,0], 6),
    # 1022am 171 / 184 test cases passed.
    ([-1,0,-2,2], 2),
    # 1038am 一瞬解答をみた。dpでやっている人がおおい。
    # その考えにいたらなかったのはなぜだ？課題
    # 他の人が自分っぽいアプローチもしていたので
    # なら完成できるんじゃない！？してやろうという気持ちで再度デバッグ
    # 1040am implemented again, see how it goes
    # 177 / 184 test cases passed.
    ([-2,0,-3,-3], 9),
    # 179 / 184 test cases passed.
    ([0, -2, 0], 0),
    #もうやけくそ、、、これは完全に滑っている
    ([-3,2,3,0,-1], 6),
    # 1136am 実装に30分くらい掛けたが、迷走中にもかかわらず前進はしたという思いあり。
    # 1137am test by submit again
    # 182 / 184 test cases passed.
    # 牛歩！この時点で、もう自分を雇いたくないね。
    # 1/ 減点ポイントはスパゲッティソース、時間かかりすぎ、固執しすぎ
    # 2/　加点ポイント、あきらめてない。
    # うわぁ〜〜〜
    ([-3,-1,3,5,-6,-6,-1,6,-3,-5,1,0,-6,-5,0,-2,6,1,0,5], 48600),
    # 181/184... degraeded..
    ([1,-2,0,1,-4,1,1,5,4,-1,6,4,1,-5,0,-1,-5,1,-6,-4], 2400),
    # 条件文, while tracing_pointのバグを修正
    # if zeroi[tracing_point-1] >= 0 and zeroi[tracing_point-1] > i:
    # finally!? ドキドキ
    # 1147am

]

"""
    ([2,-5,-2,-4,3], 24),
    [2,-10,20,-80,-240]って一回計算しますO(n)
    で
    x<=0の要素だったら、max(S[i-1], S[n-1]/S[i-1])
    っていうアルゴリズム
    がつくれそうじゃないですか？
    """

for S, expected in samples:
    ans = Solution().maxProduct(S)
    print(ans)