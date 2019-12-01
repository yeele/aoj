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

sys.setrecursionlimit(1000000)
#print (sys.getrecursionlimit())
# def rec(zan, dp):
#     # if zan % 100 == 0 or \
#     #         zan % 101 == 0 or \
#     #         zan % 102 == 0 or \
#     #         zan % 103 == 0 or \
#     #         zan % 104 == 0 or \
#     #         zan % 105 == 0:
#     #     print("zan {}".format(zan))
#     if zan == 0:
#         #print("hogaaaaaaaaaaaaaahhh ! {}".format(zan))
#         return True
#     elif zan < 0:
#         return False
#     else:
#         if zan in dp: return dp[zan]
#         # if zan-100 >= 0:
#         #     a0 = rec(zan-100, dp)
#         #     dp[zan -100] = a0
#         # if zan-101 >= 0:
#         #     a1 = rec(zan-101, dp)
#         #     dp[zan -101] = a1
#         # if zan-102 >= 0:
#         #     a2 = rec(zan-102, dp)
#         #     dp[zan -102] = a2
#         # if zan-103 >= 0:
#         #     a3 = rec(zan-103, dp)
#         #     dp[zan -103] = a3
#         # if zan-104 >= 0:
#         #     a4 = rec(zan-104, dp)
#         #     dp[zan -104] = a4
#         # if zan-105 >= 0:
#         #     a5 = rec(zan-105, dp)
#         #     dp[zan -105] = a5
#
#         a0 = rec(zan-100, dp)
#         dp[zan -100] = a0
#         a1 = rec(zan-101, dp)
#         dp[zan -101] = a1
#         a2 = rec(zan-102, dp)
#         dp[zan -102] = a2
#         a3 = rec(zan-103, dp)
#         dp[zan -103] = a3
#         a4 = rec(zan-104, dp)
#         dp[zan -104] = a4
#         a5 = rec(zan-105, dp)
#         dp[zan -105] = a5
#         #print(a0, a1, a2, a3, a4, a5)
#         ans = any(
#           [a0, a1, a2, a3, a4, a5]
#         )
#         dp[zan] = ans
#         return ans
# def sol(n):
#     dp = [False] * (n+5)
#     rec(n, dp)
#     #print("dp[%s] = %s" % (n, dp[n]))
#     return '1' if dp[n] else '0'


def sol(n):
    dp = [[False] * (n+1) for _ in range(6)]
    P = [
        100, # 100 yen
        101, # 101 yen
        102, # 102 yen
        103, # 103 yen
        104, # 104 yen
        105, # 105 yen
    ]
    for i in range(len(P)):
        for j in range(n+1): # amount
            if j % P[i] == 0:
                dp[i][j] = True
            else:
                candidates = [False]
                if j - P[i] >= 0: candidates.append(dp[i][j-P[i]])
                if i - 1 >= 0: candidates.append(dp[i-1][j])
                dp[i][j] = any(candidates)
    #for row in dp: print(row)
    #print("n {}, len(dp) {}".format(n, len(dp[0])))
    return '1' if dp[5][n] else '0'


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
    615
    """)
    print(sol(S))

    S = input_parse("""
    217
    """)
    print(sol(S))

else:
    #A, B = list(map(int, input().split()))
    S = int(input())
    print(sol(S))

    # S = input().strip()
    # print(sol(S))



