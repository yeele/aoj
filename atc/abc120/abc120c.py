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
import itertools

def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper



def str_del(str,i, j):
    str = str[:i]+str[j+1:]
    return str

#@deco
def sol(S):
    a = 0
    i = 0
    sz = len(S)
    while sz > 0 or i > sz:
        if i >= sz: break
        if i > 0:
            #print(S, i, i-1)
            if S[i] != S[i-1]:
                a += 2
                S = str_del(S, i-1, i)
                i = 0
                sz = len(S)
            else:
                i += 1
        else:
            i += 1
    return a





import logging
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.basicConfig(level=logging.ERROR, format="%(message)s")
do_submit = True
#do_submit = False
def input_parse(input_str):
    # lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    # parsed_lines = [list(map(int, line.split())) for line in lines]
    # S = parsed_lines[0][0]
    # S = parsed_lines[1]
    # return (n, S)
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    #print(lines)
    S = lines[0]
    return (S)

do_submit = False

if not do_submit:
    # n, S= input_parse("""
    # 4
    # 1 2 2 1
    # """)
    S= input_parse("""
    0011
    """)
    print(sol(S))

    S= input_parse("""
    11011010001011
    """)
    print(sol(S))

    S= input_parse("""
    0
    """)
    print(sol(S))

else:
    # a, b, c = list(map(int, input().split()))
    # print(sol(a, b, c))
    # n = int(input())
    # S = list(map(int, input().split()))
    # print(sol(S, n))
    # n, a, b, c = list(map(int, input().split()))
    # S = []
    # for i in range(n):
    #     S.append(int(input().strip()))
    # print(sol(n, a, b, c, S))
    S = input()
    print(sol(S))





