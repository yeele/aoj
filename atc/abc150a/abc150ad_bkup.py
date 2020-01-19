#-*- coding: utf-8 -*-
"""
oj dl https://atcoder.jp/contests/abc116/tasks/abc116_d -d test-d
oj test -d test-d -c "python abc116d.py"
oj test -d test-d -c "python abc116d.py" test-d/sample-3.in
"""

from collections import defaultdict
import sys
import time
import logging



def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        logging.debug('--end in %f --' % (time.time() - s))
        return ret

    return wrapper


def sol_wrong(n):
    if n <= 0: return 0
    dp = [0] * (n+1)

    dp[1] = 0
    if n == 1:
        return dp[n]
    if n == 2:
        return 1
    if n == 3:
        return 3
    # dp[2] = 1
    # dp[2] = 3
    # dp[4] = 5

    for i in range(3, n+1):
        dp[i] = dp[i-2] + i

    return dp[n]


def sol_lte():
    if n <= 0: return 0
    dp = [0] * (n+1)
    dp[1] = 0
    if n == 1:
        dp[1] = 0
        return dp[1]
    if n == 2:
        dp[2] = 1
        return dp[2]
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + i - 1
    return dp[i]


def sol(n):
    if n <= 0: return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    x = n - 1
    if x % 2 == 0: # even
        return ((x + 1) * int(x/2))
    else: # odd
        return ((x + 1) * int(x/2)) + int((x+1)/2)




do_submit = True
#do_submit = False
if do_submit:
    logging.basicConfig(level=logging.ERROR, format="%(message)s")
else:
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [[x.strip() for x in line.split()] for line in lines]
    n, k = parsed_lines[0]
    n = int(n)
    k = int(k)
    S = parsed_lines[1][0]
    return (n, k, S)


if not do_submit:
    n, k, S = input_parse("""
    14 2
    11101010110011
    """)
    print(sol(n, k, S))

    n, k, S = input_parse("""
    5 1
    00010
    """)
    print(sol(n, k, S))

    n, k, S = input_parse("""
    1 1
    1
    """)
    print(sol(n, k, S))


else:
    # str = ""
    # str += input().strip() + "\n"# n, k
    # str += input().strip() # S
    # n, k, S = input_parse(str)
    n = int(input().strip())
    print (sol(n))


