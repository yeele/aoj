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

logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
class Solution:
    @timeit
    def combinationSum2(self, nums: List[int], target: int) -> int:
        length = len(nums)
        dp = [['']*(target+1) for _ in range(length)]
        def dp_print():
            for row in dp: logging.debug(row)
        def dp_valid(i, j):
            if i < 0 or i >= length: return False
            if j < 0 or j >= target+1: return False
            return True
        def dp_get(i, j, default=''):
            if dp_valid(i, j): return dp[i][j]
            else: return default
        def dp_set(i, j, value):
            if dp_valid(i, j) and len(value) > 0:
                dp[i][j] = value
        def dp_element_empty(dp_element):
            return True if dp_element is None or len(dp_element) == 0 else False
        def dp_append(element, value):
            return ":".join([x + value for x in element.split(":")])
        def dp_concat(element1, element2):
            if element1 is None or len(element1) == 0 or element1.strip() == '': return element2
            elif element2 is None or len(element2) == 0 or element2.strip() == '': return element1
            else: return element1 + ":" + element2
        def format(text1):
            return [ int(x) for x in text1.split(",") if len(x.strip()) > 0 ]

        nums.sort()
        ans = set()
        for i in range(length):
            for j in range(target+1):
                if j == 0: continue
                if i == 4:
                    xyz = 3
                if nums[i] == j:
                    dp[i][j] = "%s,"%nums[i]
                new_p = ""
                # if dp_valid(i, j-nums[i]):
                #     p = dp_get(i, j-nums[i])
                #     if not dp_element_empty(p): # append.
                #         new_p1 = dp_append(p, "%s,"%nums[i])
                #         new_p = dp_concat(new_p, new_p1)
                for k in range(1, i+1):
                    if dp_valid(i-k, j-nums[i]):
                        p2 = dp_get(i-k, j-nums[i])
                        if not dp_element_empty(p2):
                            new_p2 = dp_append(p2, "%s,"%nums[i])
                            new_p = dp_concat(new_p, new_p2)
                dp_set(i, j,new_p)
                if j == target:
                    for element in dp[i][j].split(":"):
                        if element is not None and len(element) > 0:
                            ans.add(element)

        dp_print()
        return [format(x) for x in sorted(list(ans))]
        #return [[1,2,2], [5]]








samples = [
    #Î([10,1,2,7,6,1,5], 8, [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ] ),
    ([2,5,2,1,2], 5, [[1,2,2], [5]] ),
    ([10,1,2,7,6,1,5], 8, None)
    #([5,24,28,14,13,28,12,29,22,8,16,28,11,5,8,20,10,27,16,19,16,15,14,14,9,23,30,13,33,24,24,33,14,18,5,14,33,12,30,21,15,12,14,13,34,9,20,9,31,32,16], 29, [[]])
]
for nums, k, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum2(nums, k)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (nums, k, ans))

















class Solution_squre:
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
