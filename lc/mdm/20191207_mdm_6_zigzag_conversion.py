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

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k = numRows
        if numRows <= 1: return s
        dir = 1 #上向き
        idx = [-1] * len(s)
        j = 0
        for i in range(len(s)):
            if dir == 1:
                idx[i] = j
                j += 1
                if j == (k):#下段ヒット
                    dir = -1
                    j  = k-2
            else:
                idx[i] = j
                j -= 1
                if j == -1: #上段hit
                    dir = 1
                    j = 0+1
        #print("idx:%s" % idx)
        mapping = [ [] for _ in range(numRows)]
        #print("mapping:%s" % mapping)
        for i, index in enumerate(idx):
            #print(i, index)
            mapping[index].append(i)
        #print("mapping:%s" % mapping)
        ans = ""
        for indice in mapping:
            for i in indice:
                ans += s[i]
        return ans




samples = [
    ("PAYPALISHIRING", 3,"PAHNAPLSIIGYIR"),
]

for S, k, expected in samples:
    ans = Solution().convert(S, k)
    print(ans)
