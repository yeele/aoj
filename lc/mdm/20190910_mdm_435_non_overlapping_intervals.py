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

class Solution_gaveup:
    """
    https://leetcode.com/problems/non-overlapping-intervals/discuss/371541/Python-Greedy-Solution

    Q. どうやってgreedyがうまく行くかって判断すればいい？
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x: x[0])
        cnt = 0
        tail = intervals[0][1]
        logging.debug("1st tail: %s" % tail)
        for i in range(1, len(intervals)):
            logging.debug("intervals[%s]: %s" % (i, intervals[i]))
            if intervals[i][0] < tail:
                logging.debug("[%s][0] which is %s < %s" % (i, intervals[i][0], tail))
                if intervals[i][1] < tail:
                    logging.debug("[%s][1] which is %s < %s" % (i, intervals[i][1], tail))
                    tail = intervals[i][1]
                    logging.debug("new tail:%s assigned" % tail)
                cnt += 1
            else:
                logging.debug("[%s][0] which is %s >= %s" % (i, intervals[i][0], tail))
                tail = intervals[i][1]
        return cnt



class Solution_botsut:
    """
    implement myself after reviewing the solution above
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #intervals.sort(key=)
        # local = overlapped? or not...
        # end(above), start(below) ovalpping??
        return 0



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals is None or len(intervals) == 0: return 0
        #intervals = sorted(intervals, key = lambda x: x[0])
        intervals.sort(key = lambda x: x[0])
        end = intervals[0][1]
        overlapped = 0
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < end:
                overlapped += 1
                #以下の条件で2と3は通ります！1はダメです
                #1#end = max(e, end)
                #2#works
                end = min(e, end)
                #3#worked
                # if e < end:
                #     end = e
            else:
                end = e
        return overlapped




samples = [
    ( [[1,2],[2,3],[3,4],[1,3]], 1 ),
]

for S, expected in samples:
    ans = Solution().eraseOverlapIntervals(S)
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))

