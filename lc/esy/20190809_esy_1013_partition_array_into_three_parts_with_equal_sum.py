#-*- coding: utf-8 -*-
from typing import List

"""
20190809
O(n**2)の回答しかかけずにアウト
"""

"""
techlead tip
問題が与えられと時の条件を、
なんでそうな条件が与えられているだろうか？
そこにヒントが隠されていないか考える

例えば、今回であれば、組み合わせではなく、パーしションで
順序は変わらないという点


この問題は分析力をみられる問題ですね。

x＝３で割った数になるということ。
ジョジョは変わらないでワンタイム　パスで
合計がxが三回登場して最後まで操作が終わること

これが言えれば点数がもらえるという問題
"""

class Solution_timeexceeded:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        for i in range(len(A)-2):
            for j in range(i+1, len(A)-1):
                # print(A)
                # print(list(range(len(A))))
                # print(i, j)
                # print("1st:%s" % A[0:i+1])
                # print("2nd:%s" % A[i+1:j+1])
                # print("3rd:%s" % A[j+1:])
                if sum(A[0:i+1]) == sum(A[i+1:j+1]) == sum(A[j+1:]):
                    return True
        return False


class Solution_timeexceeded_still:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        for i in range(len(A)-2):
            first = sum(A[0:i+1])
            for j in range(i+1, len(A)-1):
                second = sum(A[i+1:j+1])
                third = total - (first + second)
                if first == second == third:
                    return True
        return False


class Solution_time_exceeded_damn_stil_bad_at_this_point_I_should_have_noticed_n2_solution_no_good:
    """
    adding backtracking
    """
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        avg = int(total /3)
        first = 0
        for i in range(len(A)-2):
            first += A[i]
            if first > avg: break
            second = 0
            for j in range(i+1, len(A)-1):
                second += A[j]
                if second > avg: break
                third = total - (first + second)
                # print(i, j)
                # print("1st:%s" % first)
                # print("2nd:%s" % second)
                # print("3rd:%s" % third)
                if first == second == third:
                    return True
        return False



class Solution_1:
    """
    I gave up and glance an other solution
    Runtime: 380 ms, faster than 21.08% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 20.4 MB, less than 6.25% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
    """
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0: return False
        avg = int(total /3)
        count = 0
        local = 0
        for i, a in enumerate(A):
            local += a
            if local == avg:
                #logging.debug("i:%s found local ans" % i)
                count += 1
                local = 0
        return count == 3 and local == 0



class Solution_2:
    """
    Runtime: 368 ms, faster than 47.53% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
    Memory Usage: 20.6 MB, less than 6.25% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
    """
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0: return False
        avg = int(total /3)
        count = 0
        local = 0
        length = len(A)
        for i in range(length):
            local += A[i]
            if local == avg:
                count += 1
                local = 0
        return count == 3 and local == 0



class Solution:
    """
    Runtime: 368 ms, faster than 47.53% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
    Memory Usage: 20.6 MB, less than 6.25% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
    """
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0: return False
        avg = int(total /3)
        count = 1
        local = 0
        length = len(A)
        for i in range(length):
            local += A[i]
            if local == avg * count:
                count += 1
        return count == 4

"""

1435pm timeexceeded...



Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
"""
samples = [
    [0,3, 7, 11],
#0,1  ^  ^
#0,2  ^    ^
#1,2     ^  ^
    [0,2,1,-6,6,-7,9,1,2,0,1], # true
    [0,2,1,-6,6,7,9,-1,2,0,1], # false
    [3,3,6,5,-2,2,5,1,-9,4],   # true
    [12,-4,16,-5,9,-3,3,8,0],  # true

]
for sample in samples:
    print(Solution().canThreePartsEqualSum(sample))

