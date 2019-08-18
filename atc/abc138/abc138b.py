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

def sol(n, S):
    ret = 0
    for s in S:
        #print(s)
        ret += (1.0 / s)
        #print (ret)
    return (1.0/ret)



do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    n = int(parsed_lines[0][0])
    S = list(map(int, parsed_lines[1]))
    # S = parsed_lines[1][0]
    # return n, k, S
    return n, S


if not do_submit:
    n, S = input_parse("""
    2
    10 30
    """)
    print(sol(n, S))

    n, S = input_parse("""
    3
    200 200 200
    """)
    print(sol(n, S))

    n, S = input_parse("""
    1
    1000
    """)
    print(sol(n, S))



else:
    n = int(input().strip())
    S = list(map(int, input().split()))
    #S = input().split()
    # print(sol(n, k, S))

    #s = input().strip()
    # S = input().strip()
    print(sol(n, S))

