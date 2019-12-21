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

def sol(a, b, c, d):
    S = [a, b, c, d]
    for i in range(1<<3):
        ttl = a
        ans = "%s" % a
        for j in range(3):
            if i & (1 << j): # '+'
                ttl += S[j+1]
                ans += "+%s" % S[j+1]
            else:
                ttl -= S[j+1]
                ans += "-%s" % S[j+1]
        if ttl == 7:
            return ans+"=7"
        else:
            assert(True)


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
    #a, b, c = list(map(int, input().split()))
    S = input()
    a = int(S[0])
    b = int(S[1])
    c = int(S[2])
    d = int(S[3])
    # S = input()
    # T = input()
    print(sol(a, b, c, d))
    # S = input().strip()
    # print(sol(S))

