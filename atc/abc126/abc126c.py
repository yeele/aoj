#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""
from collections import defaultdict
import sys
import math
from datetime import datetime
import re

def howmany_power(n, k):
    if n >= k:
        return 0
    else:
        return howmany_power(n*2, k) + 1


def sol(N, K):
    P = 0
    for n in range(1, N+1):
        if n < K:
            x = howmany_power(n, K)
            tmp = 2**x
            fst = N
            #print("n:%s, K:%s, P:%s, x:%s, tmp:%s, fst:%s" % (n, K, P, x, tmp, fst))
            P += (1/tmp)*(1/fst)
        else:
            #print("n:%s, K:%s, P:%s" % (n, K, P))
            P += (1.0/N)
    return P


do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    #print(parsed_lines)
    n = int(parsed_lines[0][0])
    k = int(parsed_lines[0][1])
    #S = parsed_lines[0][0]
    return n, k


if not do_submit:
    n, k = input_parse("""
    3 10
    """)
    print(sol(n, k))

    n, k = input_parse("""
    100000 5
    """)
    print(sol(n, k))


else:
    n, k = list(map(int, input().split()))
    #S = input()
    print(sol(n, k))

    # S = input().strip()
    # print(sol(S))



