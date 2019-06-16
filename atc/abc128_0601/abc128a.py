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

def sol(n):
    # 3 -> 3 * 60 = 180
    # 4 -> 4 * 90 = 360
    # 5 -> 5 *
    # 360 / 5 = 180 - 72 = 108 = 54 * 2 * 5
    # (180 - (360 / 5)) * 5

    return (180 - (360 / n)) * n


do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    n = int(parsed_lines[0][0])
    # k = int(parsed_lines[0][1])
    # S = parsed_lines[1][0]
    # return n, k, S
    return n


if not do_submit:
    n = input_parse("""
    3
    """)
    print(sol(n))

    n = input_parse("""
    100
    """)
    print(sol(n))

else:
    # n, k = list(map(int, input().split()))
    # S = input().split()
    # print(sol(n, k, S))
    n = int(input().strip())
    # S = input().strip()
    print(sol(n))

