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

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rank = defaultdict(int)
        for n in nums:
            rank[n] += 1
        heap = []
        for n, count in rank:
            heapq.heappush(heap, (-count, n))
        ans = []
        for i in range(k):
            count, n = heapq.heappop(heap)
            ans.append(n)
        return ans


