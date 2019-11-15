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
from itertools import permutations
class Solution:
    def findSubstring(self, S: str, words: List[str]) -> List[int]:
        sz = len(S)
        if S is None or sz == 0: return []
        if words is None or len(words) == 0: return []
        indice = []
        for W in permutations(words):
            T = "".join(W)
            indice  += self.findSubstringT(S, T, words)

        return list(set(indice))

    def findSubstringT(self, S: str, T: str, words) -> List[int]:
        sz = len(S)
        sz_w = len(words[0]) # SPEC as each word is same length
        if S is None or sz == 0: return []
        if T is None or len(T) == 0: return []
        l = r = i = 0
        indice = []
        #print("finding T -> %s" % T)
        while l < sz and r < sz:
            #print("l -> %s, r -> %s" % (l, r))
            if S[r] == T[i]:
                if r - l + 1 == len(T):
                    indice.append(l)
                    i = 0
                    l = l + 1
                    r = l
                    #print("found!!, next l -> %s, r -> %s" % (l, r))
                else:
                    r+=1
                    i+=1
            else:
                i = 0
                l = l + 1
                r = l
        return indice

samples = [
    ("barfoothefoobarman", ["foo","bar"], [0,9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    # 113/147 failed
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
    #  79/147 failed and degreade...
    ("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"], [13]),
    # 148 / 173  failed by TLE
    # that's it for now.


]


for S, words, expected in samples:
    ans = Solution().findSubstring(S, words)
    print(ans)