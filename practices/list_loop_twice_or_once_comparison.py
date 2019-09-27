#-*- coding: utf-8 -*-
import time
from collections import defaultdict

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

# items = [
#     {'item': 1, 'ts': 1569488756, 'value':500},
#     {'item': 2, 'ts': 1569488750, 'value':2}
# ]
import random

@timeit
def loop_twice(items):
    key1 = "ts"
    val1 = 8688499900
    if key1 and val1:
        ts = time.time()
        items = [i for i in items if abs(i.get(key1, 0) - ts) < val1]

    key2 = 'item'
    key3 = 'value'
    val3 = 3
    ng_items = {
        item[key2] for item in items
        if item.get(key2)
        if item.get(key3) and val3
        if item.get(key3) < val3
    }
    print(len(ng_items))
    return


import sys
@timeit
def loop_once_lambda(items):
    key1 = "ts"
    val1 = 8688499900
    if key1 and val1:
        ts = time.time()
        ts_filter = lambda doc: abs(doc.get(key1, 0) - ts) < val1
    else:
        ts_filter = lambda doc: True
    key2 = 'item'
    key3 = 'value'
    val3 = 3
    if key3 and val3:
        rr_filter = lambda doc: doc.get(key3, -sys.maxsize) < val3
    else:
        rr_filter = lambda doc: True

    ng_items = {
        item[key2] for item in items
        if item.get(key2)
        if ts_filter(item)
        if rr_filter(item)
    }
    print(len(ng_items))
    return


@timeit
def loop_once(items):
    key1 = "ts"
    val1 = 8688499900
    if key1 and val1:
        ts = time.time()
        def ts_filter(doc):
            return abs(doc.get(key1, 0) - ts) < val1
    else:
        def ts_filter(doc):
            return True
    key2 = 'item'
    key3 = 'value'
    val3 = 3
    if key3 and val3:
        def rr_filter(doc):
            return doc.get(key3, -sys.maxsize) < val3
    else:
        def rr_filter(doc):
            return True

    ng_items = {
        item[key2] for item in items
        if item.get(key2)
        if ts_filter(item)
        if rr_filter(item)
    }
    print(len(ng_items))
    return

for i in range(5):
    N = 40 * 10**i
    items = [ dict(zip(('item', 'ts', 'value'), (x, y, z)))
              for x, y, z in zip(
            range(1, N+1),
            range(1569488750, 1569488750 + (100*N), 100),
            [ random.uniform(0, 10) for _ in range(N)]
        )
    ]
    print('N:%s' % N)
    loop_twice(items)
    #loop_once(items)


def f(a):
    if a > 100:
        def F(b):
            return a + b
    else:
        def F(b):
            return a - b
    return F