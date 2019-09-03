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

def sol(S, T):
    ans = 0
    for i in range(len(S)):
        #print("i:%s, S[i]:%s, T[i]:%s" % (i, S[i], T[i]))
        if S[i] == T[i]:
            ans += 1
    return ans


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
    # n, k = list(map(int, input().split()))
    # S = input().split()
    S = input()
    T = input()
    print(sol(S, T))
    # S = input().strip()
    # print(sol(S))

