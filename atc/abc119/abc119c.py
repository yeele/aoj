#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_b -d test-b
oj test -d test-c -c "python abc116c.py"
oj test -d test-b -c "python abc116b.py" test-b/sample-3.in
"""

from collections import defaultdict
import sys
import math
import time
import itertools

def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper


def rec(T, S, m):
    logging.debug("S:%s" % S)
    for s in S:
        if s in T:
            S.remove(s)
            T.remove(s)
    i = 0
    for x in T:
        for s in S:
            if abs(s-x) <= 10:
                m += abs(s-x)
                S.remove(s)
                T.remove(x)
                return rec(T.copy(), S.copy(), m)
            else:
                for t in T:
                    mini = sys.maxsize
                    sm1 = sm2 = None
                    for comb in itertools.combinations(S, 2):
                        s1 = comb[0]
                        s2 = comb[1]
                        if abs(s1 + s2 - t) < mini:
                            mini = abs(s1 + s2 - t)
                            sm1 = s1
                            sm2 = s2
                    if sm1 != None: # found something
                        sm = sm1 + sm2
                        S.remove(sm1)
                        S.remove(sm2)
                        S.append(sm)
                        return rec(T.copy(), S.copy, m+10)
    return m




        # serach mergeable

#@deco
def sol(n, a, b, c, S):
    m = 0
    T = [a, b, c]
    return rec(T, S, m)
    #return (n, a, b, c, S)




import logging
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.basicConfig(level=logging.ERROR, format="%(message)s")
do_submit = True
#do_submit = False
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    n = parsed_lines[0][0]
    S = parsed_lines[1]
    return (n, S)


if not do_submit:
    # n, S= input_parse("""
    # 4
    # 1 2 2 1
    # """)
    n, S= input_parse("""
    5
    3 1 2 3 1
    """)
    print(sol(S, n))
else:
    # a, b, c = list(map(int, input().split()))
    # print(sol(a, b, c))
    # n = int(input())
    # S = list(map(int, input().split()))
    # print(sol(S, n))
    n, a, b, c = list(map(int, input().split()))
    S = []
    for i in range(n):
        S.append(int(input().strip()))
    print(sol(n, a, b, c, S))





