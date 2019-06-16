#-*- coding: utf-8
#  -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""
from collections import defaultdict
import sys
import math
from datetime import datetime

def sol(n, k):
    if n % k == 0:
        return 0
    else:
        md = n % k
        dv = n / k
        return md



do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    n = int(parsed_lines[0][0])
    k = int(parsed_lines[0][1])
    # S = parsed_lines[1][0]
    # return n, k, S
    return n, k


if not do_submit:
    n, k = input_parse("""
    3 2
    """)
    print(sol(n, k))

    n, k = input_parse("""
    3 1
    """)
    print(sol(n, k))
    n, k = input_parse("""
    8 5
    """)
    print(sol(n, k))

else:
    n, k= list(map(int, input().split()))
    # S = input().split()
    # print(sol(n, k, S))
    #n = int(input().strip())
    # S = input().strip()
    print(sol(n, k))

