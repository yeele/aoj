#-*- coding: utf-8 -*-
"""
"""

from collections import defaultdict
import sys


table = {
    1:3,
    2:5,
    3:5,
    4:4,
    5:5,
    6:6,
    7:3,
    8:7,
    9:6
}


def sol(n, m, A):
    """
    20 4
    3 7 8 4
    """
    dp = [[0]*(n+1) for _ in range(m+1)]
    for row in dp: print(row)
    keta = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            # js is number of match
            a = A[i-1]
            required = table[a] # number of required match
            print(i, j)
            left = j - required
            if left >= 0:
                print("%s = %s - %s. a:%s, required:%s" % (left, j, required, a, required))
                print("dp[%s][%s] = %s" % (i, j-required, dp[i][j-required]))
                if dp[i][j-required] > 0:
                    dp[i][j] = dp[i][j-required] * (10**1) + a
                    keta +=1
                else:
                    dp[i][j] = max(a, max(dp[i-1][j], dp[i][j-1]))
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for row in dp:
        print(row)
    return dp[-1][-1]




#test = False
test = True
def input_parse(input_str):
    lines = [x.strip() for x in input_str.split("\n") if x.strip()]
    parsed_lines = [list(map(int, line.split())) for line in lines]
    n, m = parsed_lines[0]
    A = parsed_lines[1]
    #print(n, m, A)
    return (n, m, A)
if test:
    n, m, A = input_parse("""
    20 4
    3 7 8 4
    """)
    print(sol(n, m, A))




else:
    n = int(input().strip())
    #n, k = map(int, input().split())
    ##S =list( map(int, "1 6 3".split()))
    #print("%s %s %s %s" % (type(n), type(k), n, k))
    S =list( map(int, input().split()))
    print(sol(n, S))


