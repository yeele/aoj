#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""

from collections import defaultdict
import sys
import time


def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s))
        return ret

    return wrapper


import itertools
#@deco
def sol_naive(n, k, S):
    maxi = 0
    for comb in itertools.combinations(S, k):
        neta = defaultdict(int)
        ttl = 0
        for t, d in comb:
            ttl += d
            neta[t] += 1
        ttl += len(neta)**2
        maxi = max(maxi, ttl)
    return maxi


def taste(S):
    return sum([d for t, d  in S])
def bonus(S):
    q = len(list(set([t for t, d  in S])))
    return q * q
def sati(S):
    return taste(S) + bonus(S)

def pick_harmless(Sa):
    logging.debug("type(Sa):%s" % type(Sa))
    cache = defaultdict(list)
    for i, (t, d) in enumerate(Sa):
        # most smallest and len(t) > 1:
        cache[t].append(d)
    for k, v in cache.items():
        if len(v) >= 2:
            non_effect_smallest = (k, min(v))
            logging.debug("before Sa:%s" % Sa)
            Sa.remove(non_effect_smallest)
            logging.debug("after  Sa:%s" % Sa)
            return Sa
    return Sa

def add_more_kind(Sa, S):
    Scopied = S.copy()
    for s in Sa:
        Scopied.remove(s)
    n = len(Sa)
    logging.debug("Scopied:%s" % Scopied)
    ts = list(set([ t for t, d in Sa]))
    Ssorted = sorted(Scopied, reverse=True, key=lambda x: x[1])
    for t, d in Ssorted:
        if t not in ts:
            logging.debug("appending maxium with different t: %s, %s" % (t, d))
            Sa.append((t, d))
            logging.debug("after  Sa:%s" % Sa)
            break
    return Sa

def sol(n, k, S):
    logging.debug("S:%s" % S)
    S.sort(key=lambda x: x[1], reverse=True)
    Sa = S[0:k]
    x = len(set([t for (t, d) in Sa]))
    maxi = sati(Sa)
    for i in range(x, k+1):
        # choose min Sushi not reducing the x
        sz_before = len(Sa)
        Sa = pick_harmless(Sa)
        if len(Sa) == sz_before: continue
        # choose max Sushi adding x+1
        Sa = add_more_kind(Sa, S)
        # update maxi
        tmp = sati(Sa)
        logging.debug("tmp:%s, current maxi:%s" % (tmp, maxi))
        maxi = max(maxi, tmp)
    return maxi


import logging

#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.basicConfig(level=logging.ERROR, format="%(message)s")
do_submit = True
#do_submit = False
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    n, k = parsed_lines[0]
    S = []
    for i in range(n):
        t, d = parsed_lines[i+1]
        S.append((t, d))
    return (n, k, S)


if not do_submit:
    n, k, S = input_parse("""
    5 3
    1 9
    1 7
    2 6
    2 5
    3 1
    """)
    print(sol(n, k, S))
else:
    n, k = list(map(int, input().split()))
    S = []
    for i in range(n):
        t, d = list(map(int, input().split()))
        S.append((t, d))
    print(sol(n, k, S))


