#-*- coding: utf-8 -*-
from typing import List
import sys
"""
"""

from collections import defaultdict
class Queue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.q = []
    def add(self, value):
        self.q.insert(0, value)
        if len(self.q) > self.maxsize:
            self.q.pop()
    def get_last(self):
        return self.q[-1]
    def get_min_max(self):
        return (self.q[0], self.q[-1])

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        if len(S) < len(T): return ""
        mini = sys.maxsize
        maxi = -sys.maxsize
        ans = S
        index_helper = defaultdict(lambda:-1)
        for i, c in enumerate(T):
            index_helper[c] = i
        # そのキャラは何個かを把握する
        nums_helper = defaultdict(lambda:0)
        for i, c in enumerate(T):
            nums_helper[c] += 1
        memo: dict = {}
        for c, n in nums_helper.items():
            q = Queue(n)
            for _ in range(n):
                q.add(-1)
            i = index_helper[c]
            memo[i] = q
        counter = 0
        for i, c in enumerate(S):
            idx = index_helper[c]
            if idx == -1: continue # T以外のキャラ

            #local = max(i, max(memo[idx].q)) # ってか常にiだとおもう。なので　local = i が成立
            local = i
            if memo[idx].get_last() == -1:
                counter+=1 # 初めて見つかったということで。
            memo[idx].add(local)
            local_mini, local_max = memo[idx].get_min_max()
            # mini = min(mini, local_mini)
            # maxi = max(maxi, local_max)
            # ここでハッと気づく。
            # 2156pmデグレった
            mini = min([q.q[-1] for c, q in memo.items()]) # O(T)からO(1)に改善できたので通りました！
            maxi = max([q.q[0] for c, q in memo.items()])
            # mini = min([min(q.q) for c, q in memo.items()]) # O(T)なんんで、これだとO(N)に届かずRTEくらいそう
            # maxi = max([max(q.q) for c, q in memo.items()])
            if counter == len(T):
                if (maxi+1) - mini < len(ans):
                    ans = S[mini:maxi+1]
        return ans if counter == len(T) else ""


class Solution_works_only_non_duplicated_input:
    """
    # 重複にも対応しないといけない 2108pm
    # ここはこれまでのでーた構造dict(int)では無理になって　
    # dict(queue)に変更しないといけなくなったので実装にも時間が
    # かかるかもしれない。デグレもある。
    # まさにhardにふさわしい問題だとおもう 2115pm
    ("aaa", "aa", ""),
    """
    def minWindow(self, S: str, T: str) -> str:
        if len(S) < len(T): return ""
        memo = [-1] * len(T)
        mini = sys.maxsize
        maxi = -sys.maxsize
        ans = S
        index_helper = defaultdict(lambda:-1)
        for i, c in enumerate(T):
            index_helper[c] = i
        counter = 0
        for i, c in enumerate(S):
            idx = index_helper[c]
            if idx == -1: continue # T以外のキャラ

            local = max(i, memo[idx])
            if memo[idx] == -1:
                counter+=1 # 初めて見つかったということで。
            memo[idx] = max(memo[idx], local)
            # mini = min(mini, local)
            # maxi = max(maxi, local) # こっちのが高速だが間違ってるのでまずは。
            mini = min(memo) # O(T)なんんで、これだとO(N)に届かずRTEくらいそう
            maxi = max(memo)
            if counter == len(T):
                if (maxi+1) - mini < len(ans):
                    ans = S[mini:maxi+1]
        return ans if counter == len(T) else ""




samples = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "aa", ""),
    ("a", "b", ""),
    # # 重複にも対応しないといけない 2108pm
    # # 124 / 268 passed
    # # ここはこれまでのでーた構造dict(int)では無理になって　
    # # dict(queue)に変更しないといけなくなったので実装にも時間が
    # # かかるかもしれない。デグレもある。
    # # まさにhardにふさわしい問題だとおもう 2115pm
    # ("aa", "aa", ""),
    # 267 / 268 LTE
    # お、よそうどうり  2147pm
    # 2156pmデグレった
    ("aa", "aa", "aa"),
    # 2159pm minはq.q[-1]でmaxはq.q[0]でした。逆でした
    # 2208pmすでに通ったけど local = iでさらに半分のruntimeで。
    # しかし、まだまだ遅いよう

]
for S, T, expected in samples:
    print("-"*20)
    ans = Solution().minWindow(S, T)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (S, T, ans, expected)
    print("(%s, %s) = %s as expected!" % (S, T, ans))
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    #print("(%s) = %s as expected!" % (S, ans))

