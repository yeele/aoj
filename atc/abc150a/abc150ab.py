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
def sol(n, X, L):
    Cs = []
    for i in range(n):
        Cs.append( (X[i] - L[i], X[i] + L[i] ) )
    mini = sys.maxsize
    m, n = None, None
    counter = 0
    Cs.sort(key=lambda x : x[0])
    for a, b in Cs:
        if m is None:
            counter += 1
        elif a <= m and n <= b:
            counter += 1
        elif n <= a:
            counter += 1
        # 被っている部分の更新
        if m is None: m, n = a, b
        elif b < n: m, n = min(b, n), n
        elif a < n: m, n = n, b
        else: m, n = max(a,n), b
    return counter





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
    n = int(input())
    X = []
    L = []
    for i in range(n):
        x, l = list(map(int, input().split()))
        X.append(x)
        L.append(l)

    print(sol(n, X, L))

    # S = input().strip()
    # print(sol(S))



