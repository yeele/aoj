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
#sys.setrecursionlimit(314159265)

def sol_nn(N):
    if N < 2: return 1

    ans = 2 * math.factorial(N/2)
    print(ans)
    counter = 0
    while ans % 10 == 0:
        counter += 1
        ans //= 10

    #print(ans)
    return counter

def sol(N):
    stack = [1, 1]
    for i in range(1, N+1):
        #print("i:{} stack:{}".format(i, stack))
        n2 = stack[0]
        #print("poped, so i:{} stack:{}".format(i, stack))
        tmp = i * n2
        stack[0] = stack[1]
        stack[1] = tmp
    ans = stack[1]

    #print(ans)
    #ans = f(N)
    counter = 0
    while ans % 10 == 0:
        counter += 1
        ans //= 10

    #print(ans)
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
    n = int(input())
    #S = list(map(int, input().split()))
    #S = input()
    print(sol(n))

    # S = input().strip()
    # print(sol(S))



