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

@timeit
def loop_twice():
    items = [{'item': 1, 'ts': 1569488756}, {'item': 2, 'ts': 1569488750}]
    key1 = "ts"
    val1 = 86400
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


@timeit
def loop_once():
    items = [{'item': 1, 'ts': 1569488756}, {'item': 2, 'ts': 1569488750}]
    key1 = "ts"
    val1 = 86400

    # Todo. make loop once :)

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

loop_twice()
loop_once()