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

def sol(a, b, c):
    return min(int(b/a), c)


do_submit = True
do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    a, b, c = parsed_lines[0]
    return a, b, c


if not do_submit:
    a, b, c = input_parse("""
    2 11 4
    """)
    print(sol(a, b, c))
else:
    a, b, c = list(map(int, input().split()))
    print(sol(a, b, c))
    # S = input().strip()
    # print(sol(S))

