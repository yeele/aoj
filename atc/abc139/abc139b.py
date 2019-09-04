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
def sol(a, b):
    c = 1
    ans = 0
    if c >= b: return ans

    while c < b:
        c += a - 1
        ans += 1
    return ans



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
    A, B = list(map(int, input().split()))
    #S = input()
    print(sol(A, B))

    # S = input().strip()
    # print(sol(S))



