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

W = "love"
L = ["evol", "vole", "volvell", "lowa", "lover", "levo", "love", "lvvo"]

pattern = {c for c in W}
print(pattern)

def is_similar(word, pattern):
    my_pattern =  {c for c in word}
    if len(my_pattern) > 0 and len(my_pattern) == len(pattern):
        ans = all([c in my_pattern for c in pattern])
        return ans
    return False

A = []
for word in L:
    if is_similar(word, pattern):
      A.append(word)

print("W:%s"%W)
print("L:%s"%L)
print("A:%s"%A)
print(len(A))
