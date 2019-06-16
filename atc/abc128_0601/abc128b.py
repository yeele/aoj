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

def sol(S):
    # oxoxoxoxoxoxox
    c = 0
    for s in S:
        if s == 'o': c+=1
    return 'YES' if 15 - len(S) + c >= 8 else 'NO'


do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    #n = int(parsed_lines[0][0])
    S = parsed_lines[0][0]
    # k = int(parsed_lines[0][1])
    # S = parsed_lines[1][0]
    # return n, k, S
    return S


if not do_submit:
    S = input_parse("""
    oxoxoxoxoxoxox
    """)
    print(sol(S))

    S = input_parse("""
    xxxxxxxx
    """)
    print(sol(S))

else:
    # n, k = list(map(int, input().split()))
    # S = input().split()
    # print(sol(n, k, S))
    S = input().strip()
    # S = input().strip()
    print(sol(S))

