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

cache = defaultdict(int)
def rec(cur, n, A, chosen=""):
    global cache
    print(cur, n, A, chosen)
    if cur in cache.keys() and cache[cur] > 0:
        tmp = cache[cur]
        print("YES!!(cached)" + chosen + " and cache says " + str(tmp))
        cache[cur] = tmp + 1
        print("cache(cached):%s" % cache)
        return 1 +  tmp
    elif cur in A:
        cache[cur] = 0
        return 0
    else:
        if cur > n:
            return 0
        elif cur == n:
            print("YES!!" + chosen)
            cache[cur] = 1

            return 1
        else:
            a = rec(cur + 1, n, A, chosen+",%s"%(cur+1))
            b = rec(cur + 2, n, A, chosen+",%s"%(cur+2))
            if a + b > 0:
                cache[cur] = max(a, b)
                print("cache:%s" % cache)
            return max(a, b)


def sol2(n, m, A):
    global cache
    cache = defaultdict(int)
    total = rec(0, n, A, "0")
    print("total is %s" % total)
    return total % (10**9 + 7)

def sol(n, m, A):
    print("------- asc ----------")
    x1 = sol_asc(n, m, A)
    print("======= desc =========")
    x2 = sol_desc(n, m, A)
    print("asc:%s, desc:%s" % (x1, x2))
    return

def sol_asc(n, m, A):
    # 0 , 1, 2, 3, 4, 5, 6
    mod = 1000000007
    dp = [1] + [0]*n
    #print("status(initially): %s" % dp)
    for i in range(n+1):

        if i == 0: dp[i] = 1
        #elif i == 1: dp[i] = 1 # fucking BUG!!!!
        elif i in A: dp[i] = 0
        elif i == 1: dp[i] = 1 # fucking BUG FIXED bt changing if order!!!!
        else:
            # print("dp[%s];%s = dp[%s];%s + dp[%s];%s" % (
            #     i, dp[i], i-1, dp[i-1], i-2, dp[i-2])
            # )
            dp[i] = (dp[i-1] + dp[i-2]) % mod
        print("status: %s" % dp)
    return dp[-1]

def sol_desc(n, m, A):
    # 0 , 1, 2, 3, 4, 5, 6
    mod = 1000000007
    dp =  [0]*(n+3)
    #print("status(initially): %s" % dp)
    for i in range(n, -1, -1):
        if i == n: dp[i] = 1
        elif i in A: dp[i] = 0
        else:
            dp[i] = dp[i+1] + dp[i+2]
            #dp[i] %= mod
        print("i:%s, dp:%s" % (i, dp))
    return dp[0] % mod


def sol3(n, m, A):
    dp = [0, 0] + [0]*n
    print("dp:%s"%dp)

    for i in range(2, n+2):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = 1 + max(dp[i-1], dp[i-2])
        print("i:%s, dp[%s]:%s" % (i, i, dp[i]))
        print(dp)
    total = dp[-1]
    return total % (10**9 + 7)


do_submit = True
do_submit = False

def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(str, line.split())) for line in lines]
    #print(parsed_lines)
    n = int(parsed_lines[0][0])
    m = int(parsed_lines[0][1])
    #print(n, m)
    A = []
    for i in range(1, m+1):
        A.append(int(parsed_lines[i][0]))
    print(n, m, A)

    # W = [int(x) for x in parsed_lines[1]]
    # k = int(parsed_lines[0][1])
    # S = parsed_lines[1][0]
    # return n, k, S
    return n, m, A


if not do_submit:
    n, m, A = input_parse("""
    6 1
    3
    """)
    #print(sol(n, m, A))

    n, m, A = input_parse("""
    10 2
    4
    5
    """)
    #print(sol(n, m, A))

    n, m, A = input_parse("""
    10 5
    1
    23
    45
    67
    89
    """)
    print(sol(n, m, A))

    n, m, A = input_parse("""
    100 5
    1
    23
    45
    67
    89
    """)
    print(sol(n, m, A))


else:
    n = int(input())
    W = list(map(int, input().split()))
    # print(sol(n, k, S))
    #S = input().strip()
    # S = input().strip()
    print(sol(n, W))

