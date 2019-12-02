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
import math
def sol(n):
    A = math.floor(math.ceil(n/1.08) * 1.08) == n
    if A:
        return math.ceil(n/1.08)
    B = math.floor(math.floor(n/1.08) * 1.08) == n
    if B:
        return math.floor(n/1.08)
    return ":("



do_submit = True
#do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    print(parsed_lines)
    n = int(parsed_lines[0][0])
    #k = int(parsed_lines[0][1])
    #S = parsed_lines[0][0]
    return n


if not do_submit:
    S = input_parse("""
    432
    """)
    print(sol(S))

    S = input_parse("""
    1079
    """)
    print(sol(S))

    S = input_parse("""
    1001
    """)
    print(sol(S))



else:
    #A, B = list(map(int, input().split()))
    S = int(input())
    print(sol(S))

    # S = input().strip()
    # print(sol(S))



