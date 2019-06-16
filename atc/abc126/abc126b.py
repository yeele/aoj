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

def sol(S):
    #YYMM, MMYY, AMBIGUOUS, NA のうち正しいものを出力せよ。
    if re.match("^[0][0][0][0]$", S):
        return 'NA'
    if re.match("^[0][0][0-1][0-2]$", S):
        return 'YYMM'
    if re.match("^[0-1][0-2][0][0]$", S):
        return 'MMYY'
    elif re.match("^[0-1][0-2][0-1][0-2]$", S):
        return 'AMBIGUOUS'
    elif re.match("^[0-9][0-9][1][0-2]$", S):
        return 'YYMM'
    elif re.match("^[0-9][0-9][0][1-9]$", S):
        return 'YYMM'
    elif re.match("^[1][0-2][0-9][0-9]$", S):
        return 'MMYY'
    elif re.match("^[0][1-9][0-9][0-9]$", S):
        return 'MMYY'
    else:
        return 'NA'


do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    # n = int(parsed_lines[0][0])
    # k = int(parsed_lines[0][1])
    S = parsed_lines[0][0]
    return S


if not do_submit:
    S = input_parse("""
    1905
    """)
    print(sol(S))

    S = input_parse("""
    0112
    """)
    print(sol(S))

    S = input_parse("""
    1700
    """)
    print(sol(S))

    S = input_parse("""
    0000
    """)
    print(sol(S))

    S = input_parse("""
    1001
    """)
    print(sol(S))



else:
    #n, k = list(map(int, input().split()))
    S = input()
    print(sol(S))

    # S = input().strip()
    # print(sol(S))



