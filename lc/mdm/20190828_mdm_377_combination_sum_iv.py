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
    @timeit
    def combinationSum4(self, nums: int, target: int) -> int:
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

        ans = set()
        for i in range(length):
            for j in range(target+1):
                if j == 0: continue
                if nums[i] == j:
                    dp[i][j] = "%s,"%nums[i]
                new_p = ""
                if dp_valid(i, j-nums[i]):
                    p = dp_get(i, j-nums[i])
                    if not dp_element_empty(p): # append.
                        new_p1 = dp_append(p, "%s,"%nums[i])
                        new_p = dp_concat(new_p, new_p1)
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
        unique_combs = [format(x) for x in sorted(list(ans))]
        comb_num = 0
        for comb in unique_combs:
            #comb_num += len(list(itertools.permutations(comb)))
            tmp = nCr(comb)
            logging.debug("nCr(%s) is %s " % (comb, tmp))
            comb_num += tmp
            # c = defaultdict(int)
            # for x in comb:
            #     c[x] += 1
            # #kaburi = sum(filter(lambda x: x != 1, c.values()))
            # kaburi = min([0] + list(filter(lambda x: x != 1, c.values())))
            # tmp = ncr(len(comb), 1 if kaburi==0 else kaburi)
            # logging.debug("comb:%s is %sC%s = %s" % (comb, len(comb), kaburi, tmp))
            # comb_num += tmp

        return int(comb_num)



#--- helper ---
import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def nCr(arr, i=0): # arr is sorted
    if i > len(arr): return 0
    N = len(arr[i:])
    if N <= 0: return 1
    elif N == 1: return 1
    else:
        pre = arr[i]
        y = 1
        for j in range(i+1, len(arr)):
            x = arr[j]
            if x == pre: y += 1
            else: break
            pre = x
        logging.debug("arr:%s, i:%s, y:%s" % (arr[i:], i, y))
        return ncr(N, y) * nCr(arr, i+y)

#--- helper ---

samples = [
    ([1, 2, 3], 4, 7),
    #([1, 2], 10, 89),
]
for k, n, expected in samples:
    print("-"*20)
    ans = Solution().combinationSum4(k, n)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (nums, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (k, n, ans))

print(nCr([1, 1, 2]))
print(nCr([1, 1, 1, 2, 2, 3]))
print(nCr([1, 1, 1, 1]))





