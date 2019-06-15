#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_b -d test-b
oj test -d test-c -c "python abc116c.py"
oj test -d test-b -c "python abc116b.py" test-b/sample-3.in
"""

from collections import defaultdict
import sys
import math
import time

def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper


#@deco
def sol(S, n):
    return (S, n)



import logging
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.basicConfig(level=logging.ERROR, format="%(message)s")
do_submit = True
do_submit = False
def input_parse(input_str):

    def to_intgers(strs:list):
        return map(int, strs)
    def get_first_int(strs:list):
        A = map(int, strs)
        return A[0]

    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [[s.strip() for s in line.split()] for line in lines]
    """
    parsed_lines = [
    ["5", "3"],
    ["10"],
    ["15"],
    ["11"],
    ["14"],
    ["12"]
    """
    n, k = to_intgers(parsed_lines[0][0])
    H = parsed_lines[1]
    return (n, S)


if not do_submit:
    # n, S= input_parse("""
    # 4
    # 1 2 2 1
    # """)
    n, S= input_parse("""
    5 3
    10
    15
    11
    14
    12
    """)
    print(sol(S, n))
else:
    # a, b, c = list(map(int, input().split()))
    # print(sol(a, b, c))
    n = int(input())
    S = list(map(int, input().split()))
    print(sol(S, n))


