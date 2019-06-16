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
    #1 25 25 50
    1st: win, 0.5
    1st: draw 0.5 , 2nd: win 0.5
    0.75

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



