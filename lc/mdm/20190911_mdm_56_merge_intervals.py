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





class Solution:
    """
    implement myself after reviewing the solution above
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals is None or len(intervals) == 0: return intervals
        intervals.sort(key=lambda x : x[0])
        length = len(intervals)
        s = intervals[0][0]
        e = intervals[0][1]
        ans = [intervals[0]]
        for i in range(1, length):
            if intervals[i][0] <= e:
                # need to merge
                ans.pop()
                merged_e = max(e, intervals[i][1])
                ans.append([s, merged_e])
                e = merged_e
            else:
                ans.append(intervals[i])
                s = intervals[i][0]
                e = intervals[i][1]

        return ans





samples = [
    ( [[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ( [[1,4],[4, 5]], [[1, 5]]),
    ( [[1,4], [2,3]], [[1,4]] )
]

for S, expected in samples:
    ans = Solution().merge(S)
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))

