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

def sol(a, b, c):
    big = max(a, b)
    if c % big == 0: return c // big
    else: return (c // big) + 1
    #return 1 + 2 + 3 - a - b
    #if a + b + c <= 21: return 'win'
    #else: return 'bust'



do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    n = int(parsed_lines[0][0])
    k = int(parsed_lines[0][1])
    S = parsed_lines[1][0]
    return n, k, S


if not do_submit:
    a, b, c = input_parse("""
    3 1
    ABC
    """)
    print(sol(a, b, c))

    a, b, c = input_parse("""
    4 3
    CABA
    """)
    print(sol(a, b, c))

else:
    #a, b, c = list(map(int, input().split()))
    # S = input().split()
    a = int(input())
    b = int(input())
    c = int(input())
    # T = input()
    print(sol(a, b, c))
    # S = input().strip()
    # print(sol(S))

