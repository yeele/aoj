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
    def combinationSum3(self, K: int, target: int) -> List[List[int]]:
        nums = list(range(1, 10))
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
                            if len(element) == K*2:
                                ans.add(element)

        dp_print()
        return [format(x) for x in sorted(list(ans))]
        #return [[1,2,2], [5]]








samples = [
    #([1, 2, 3, 4, 5, ], 5, [[1,2,2], [5]] ),
    #([10,1,2,7,6,1,5], 8, None)
    #(3, 7, [[1, 2, 4]]),
    (3, 2, []),
]
for k, n, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum3(k, n)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (k, n, ans))





