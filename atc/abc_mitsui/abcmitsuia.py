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

def sol(m1, d1, m2, d2):
    return 0 if m1 == m2 else 1


do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    m1 = int(parsed_lines[0][0])
    d1 = int(parsed_lines[0][1])
    m2 = int(parsed_lines[1][0])
    d2 = int(parsed_lines[1][1])
    #S = parsed_lines[1][0]
    return m1, d1, m2, d2


if not do_submit:
    m1, d1, m2, d2 = input_parse("""
    11 16
    11 17
    """)
    print(sol(m1, d1, m2, d2))

    m1, d1, m2, d2 = input_parse("""
    11 30
    12 1
    """)
    print(sol(m1, d1, m2, d2))

else:
    m1, d1 = list(map(int, input().split()))
    m2, d2 = list(map(int, input().split()))
    # S = input().split()
    # S = input()
    # T = input()
    print(sol(m1, d1, m2, d2))
    # S = input().strip()
    # print(sol(S))

