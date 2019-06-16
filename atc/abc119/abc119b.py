#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""
from collections import defaultdict
import sys
import math


def sol(n, a, b, c, S):
    return (n, a, b, c, S)


do_submit = True


def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    a, b, c = parsed_lines[0]
    return a, b, c


if not do_submit:
    a, b, c = input_parse("""
    45 28 53
    """)
    print(sol(a, b, c))
else:
    n, a, b, c = list(map(int, input().split()))
    S = []
    for i in len(n):
        S.append(int(input().strip()))
    print(sol(n, a, b, c, S))

