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

def sol(a, s):
    if a >= 3200:
        return s
    else:
        return 'red'



do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    a = int(parsed_lines[0][0])
    s = parsed_lines[1][0]
    # S = parsed_lines[1][0]
    # return n, k, S
    return a, s


if not do_submit:
    a, s = input_parse("""
    3200
    pink
    """)
    print(sol(a, s))

else:
    #n, k= list(map(int, input().split()))
    #S = input().split()
    # print(sol(n, k, S))
    a = int(input().strip())
    s = input().strip()
    # S = input().strip()
    print(sol(a, s))

