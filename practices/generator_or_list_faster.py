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


import random

@timeit
def with_generator(rows):
    ans = any(
        row['a'] > 20 for row in rows
        if 'a' in row
    )
    return ans

@timeit
def with_list(rows):
    ans = any([
        row['a'] > 20 for row in rows
        if 'a' in row
    ])
    return ans


for i in range(5):
    N = 40 * 10**i
    rows = [ dict(zip(('c', 'b', 'a'), (x, y, z)))
              for x, y, z in zip(
            range(1, N+1),
            range(1569488750, 1569488750 + (100*N), 100),
            [ random.uniform(0, 10) for _ in range(N)]
        )
    ]
    print('-------- N:%s --------' % N)
    with_generator(rows)
    #with_list(rows)

