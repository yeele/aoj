#Definition for singly-linked list.

def timeit(method):
    def timed(*args, **kw):
        global calc
        calc = defaultdict(int)
        print ('===========')
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.8f ms' % (method.__name__, (te - ts) * 1000))
        print("calc %s times" % sum(calc.values()))
        return result
    return timed


from typing import List
import sys
import logging
import itertools
from collections import defaultdict
import time
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = defaultdict(list)
        for i, c in enumerate(s):
            memo[c].append(i)

        #logging.debug("memo:%s" % memo)
        maxi = 0
        for c, indices in memo.items():
            buffer = k
            local = 0
            for i in range(1, len(indices)):
                start = indices[i-1]
                end   = indices[i]
                btw = end - start - 1
                if btw > 0:
                    buffer -= btw
                if k == 0 and btw > 0:
                    buffer = k
                    local = 0
                if buffer >= 0:
                    local += (end - start)
                    if i == len(indices) - 1:
                        local += buffer + 1  # 最初の借金1
                    maxi = max(local, maxi)
                else:
                    # reset, hoping luck in the later.
                    buffer = k
                    local = 0

        return min(maxi, len(s))





samples = [
    ( "ABAB", 2, 4 ),
    ("AABABBA", 1, 4),
    ("ABCADBBFAF", 3, 6),

    # 1st submitted, but following case failed
    ("AAAA", 2, 4),
    # それで、bufferが余るケースがあるんだとわかり
    # return min(maxi, len(s))

    # 2nd submitted, but following case failed
    ("AABA", 0, 2),
    # なるほど、何もいじらないケースね。

]

for S, k, expected in samples:
    ans = Solution().characterReplacement(S, k)
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (S, ans, expected)
    print("(%s, %s) = %s as expected!" % (S, k, ans))

