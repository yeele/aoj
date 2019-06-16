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

def sol(n, W):
    # oxoxoxoxoxoxox
    mini = sys.maxsize
    #print(n, W)
    for i in range(len(W)):
        #print(i)
        mini = min(abs(sum(W[0:i]) - sum(W[i:len(W)])), mini)
    #print("end")
    return mini


do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    #print(parsed_lines)
    n = int(parsed_lines[0][0])
    W = [int(x) for x in parsed_lines[1]]
    # k = int(parsed_lines[0][1])
    # S = parsed_lines[1][0]
    # return n, k, S
    return n, W


if not do_submit:
    n, W = input_parse("""
    3
    1 2 3
    """)
    print(sol(n, W))

    n, W = input_parse("""
    4
    1 3 1 1
    """)
    print(sol(n, W))

else:
    n = int(input())
    W = list(map(int, input().split()))
    # print(sol(n, k, S))
    #S = input().strip()
    # S = input().strip()
    print(sol(n, W))

