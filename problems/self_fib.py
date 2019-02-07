#-*- coding: utf-8 -*-
"""
http://tango-ruby.hatenablog.com/entry/2016/10/20/172918
"""
import time
from collections import defaultdict

calc = defaultdict(int)

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

"""
O(2**n)
"""

def fib1(n):
    calc[n] += 1
    if n <= 2: return n
    else: return fib1(n-2) + fib1(n-1)

dp = {}
def fib2(n):
    global dp
    if n in dp.keys(): return dp[n]
    else:
        calc[n] += 1
        if n <= 2:
            dp[n] = n
            return n
        else:
            ret = fib2(n-2) + fib2(n-1)
            dp[n] = ret
            return ret

def fib3(n):
    if n == 0: return 1
    f1 = f2 = f3 = 1
    for i in range(n-1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3


@timeit
def get_fib1(n):
    return fib1(n)

@timeit
def get_fib2(n):
    return fib2(n)

@timeit
def get_fib3(n):
    return fib3(n)

# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))
print("fib() is %s" % get_fib1(30))
print("fib() is %s" % get_fib2(30))
print("fib() is %s" % get_fib3(30))



"""
0+1, 1
1+1, 2
1+2, 3
2+3, 5
3+5, 8
5+8, 13

if n == 0: 0
n == 1: 0+1
n == 2: 1+1
fib(n) = fib(n-2) + fib(n-1)
"""