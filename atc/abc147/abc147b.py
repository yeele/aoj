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
import math
def sol(S):
    sz = len(S)
    if sz == 0: return 0

    if sz % 2 == 0:
        l = (sz // 2) - 1
        r = (sz // 2)
    else:
        l = r = (sz //2)
    c = 0
    while l >= 0:
        if S[l] != S[r]:
            c += 1
        l -= 1
        r += 1
    return c




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
    #A, B = list(map(int, input().split()))
    S = input()
    print(sol(S))

    # S = input().strip()
    # print(sol(S))



