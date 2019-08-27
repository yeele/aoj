#Definition for singly-linked list.
from typing import List
import sys

import logging
#logging.basicConfig(level=logging.WARN, format="%(message)s")
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
import itertools
from collections import defaultdict
import time
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

class Solution:
    def __init__(self):
        self.ans = []
        self.dp = defaultdict(list)
        self.cache = True
        self.hit = 0
        self.calls = 0
    @timeit
    def combinationSum2(self, nums: List[int], target: int) -> int:
        self.hit = 0
        self.calls = 0
        self.ans = []
        nums.sort()
        self.rec(nums, target, 0, "")
        # how to remove duplicate from list of list since set doesn't work
        # https://stackoverflow.com/questions/2213923/removing-duplicates-from-a-list-of-lists
        self.ans.sort()
        logging.info("cache hit:%s / calls:%s" % (self.hit, self.calls))
        #logging.info("dp:%s"%self.dp)
        return list(k for k,_ in itertools.groupby(self.ans))

    def csv_to_list(self, text):
        return [int(x.strip()) for x in text.split(",") if x.strip() is not ""]

    def cachey(self, S, target, i):
        key = ",".join([str(x) for x in S[i:]]) + ":" + str(target)
        return key

    def rec(self, S: List[int], target: int, i, sofar: str):
        self.calls += 1
        #logging.debug("rec(%s, %s, %s, %s)" % (S, target, i, sofar))
        if self.cachey(S, target,i) in self.dp[self.cachey(S, target,i)] and self.cache:
            self.hit += 1
            return self.dp[self.cachey(S,target,i)]
        length = len(S)
        if target == 0:
            self.ans.append(self.csv_to_list(sofar))
            self.dp[self.cachey(S,target, i)] = self.ans[:]
            return
        elif target < 0:
            return
        else:
            if i >= length: return
            x = S[i]
            self.rec(S, target-x, i+1, sofar + "%s,"%x )
            self.dp[self.cachey(S, target-x, i+1)] = self.ans[:]
            self.rec(S, target, i+1, sofar)
            self.dp[self.cachey(S, target, i+1)] = self.ans[:]







samples = [
    #Î([10,1,2,7,6,1,5], 8, [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ] ),
    ([2,5,2,1,2], 5, [[1,2,2], [5]] ),
    ([5,24,28,14,13,28,12,29,22,8,16,28,11,5,8,20,10,27,16,19,16,15,14,14,9,23,30,13,33,24,24,33,14,18,5,14,33,12,30,21,15,12,14,13,34,9,20,9,31,32,16], 29, [[]])
]
for nums, k, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum2(nums, k)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (nums, k, ans))
