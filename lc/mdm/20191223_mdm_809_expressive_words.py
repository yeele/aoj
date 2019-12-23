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
from collections import defaultdict

# question was asked by google phone interview
# https://leetcode.com/discuss/interview-question/455534/Google-or-Phone-or-Expressive-Words
# https://leetcode.com/problems/expressive-words/
class Solution_mycode_failed:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        #print(S, words)
        def is_stretchy(S, word):
            i = j = 0
            if S[i] != word[j]: return False
            if len(S) <= len(word)+1: return False
            i = j = 1
            while not(i == len(S) and j == len(word)):
                if j >= len(word): j = len(word) - 1
                if i >= len(S): i = len(S) - 1
                if S[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    if S[i-1] == S[i]:
                        stretchy_cnt = 1
                        k = i
                        while S[k-2] == S[i] and k >= 0:
                            k -= 1
                            stretchy_cnt += 1
                        while S[i-1] == S[i]:
                            stretchy_cnt += 1
                            i += 1
                        if stretchy_cnt < 3:
                            return False
                    else:
                        return False
            return True

        counter = 0
        for word in words:
            if is_stretchy(S, word):
                counter += 1
        return counter

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        """
        heeellooo
        hello
        まずはsの登場文字順にrepeat数をかぞえましょう
        (h:1, e:3, l:2, o:3)
        (h:1, e:1, l:2, o:1)
        配列の長さも当然おなじ
        文字が全部同じであること。
        上のほうが、長さが3以上あること。
        下の文字のほうが、常に小さい
        """
        def c_count(S):
            if S is None or len(S) == 0: return []
            cc = []
            moji = S[0]
            moji_idx = 0
            for i in range(len(S)+1):
                if i < len(S) and S[i] == moji:
                    pass
                else:
                    cc.append((moji, i - moji_idx))
                    if i < len(S):
                        moji = S[i]
                        moji_idx = i
            return cc

        #def is_stretcy(S, T):
        def is_stretcy(cc1, cc2):
            # cc1 = c_count(S)
            # cc2 = c_count(T)
            # cc is list of tuple('c': int)
            # print(cc1)
            # print(cc2)

            if len(cc1) != len(cc2): return False
            for i in range(len(cc1)):
                if cc1[i][0] != cc2[i][0]: return False
                if cc1[i][1] != cc2[i][1] and cc1[i][1] < 3: return False
                if cc1[i][1] < cc2[i][1]: return False
            return True

        counter = 0
        cc1 = c_count(S)
        for T in words:
            cc2 = c_count(T)
            if is_stretcy(cc1, cc2):
                counter += 1
        return counter

samples = [
    ("heeellooo", ["hello"], 1),
    ("heeellooo", ["hello", "hi", "helo"], 1),
    ("feeeeel", ["feel", "cool"], 1),
    #15/29 failed
    ("aaa", ["aaaa"], 0),
    #18/29 failed
    #問題の理解が齟齬が判明
    #https://leetcode.com/submissions/detail/287973770/
    ("dddiiiinnssssssoooo",
    ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"], 3),
]

for S, words, expected in samples:
    ans = Solution().expressiveWords(S, words)
    print(ans)


