#-*- coding: utf-8 -*-
from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter(indent=4)
COUNTER = defaultdict(int)
CACHE = defaultdict(int)
import logging, time
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper

def fibo(n):
    """
    0 1 1 2 3 5 8 13 21 34

    Args:
        n (int): Nth fibonacci

    Returns:
        bool: give Nt5h fibonacci value

    """
    COUNTER[n]+= 1
    #print("fibo(%s)" % n)
    if n <= 1: return n
    if n not in CACHE:
        CACHE[n] = fibo(n-2) + fibo(n-1)
    return CACHE[n]

@deco
def test():
    print(fibo(20))

test()
pp.pprint(COUNTER)


