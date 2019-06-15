#-*- coding: utf-8 -*-
"""
https://techdevguide.withgoogle.com/paths/foundational/sequence-2/find-longest-word-in-dictionary-that-subsequence-of-given-string/#code-challenge


"""


def lcs_v1(a, b):
    dp = [[0] * (len(b)+1) for _ in range((len(a)+1))]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 or j == 0: dp[i][j] = 0
            elif a[i-1] == b[j-1]:
                #dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + 1
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    for row in dp:
        print (row)
    return dp[-1][-1]

def lcs(S, W):

    dp = [[0] * (len(S)+1) for _ in range(len(W)+1)]
    for i, w in enumerate(W):
        i+=1
        for j, s in enumerate(S):
            j+=1
            if s == w:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # for row in dp:
    #     print (row)
    return dp[-1][-1]



def sol(S, D):
    maxi = 0
    ans = None
    for W in D:
        sz = lcs(S, W)
        if sz > 0: print(S, W, sz)
        if sz > maxi:
            maxi = sz
            ans = W
    return ans


# import sys
# sys.setrecursionlimit(314159265)
test = False
test = True
if test:
    # n, k = 5, 5
    #S =list( map(int, "4 2 6".split()))

    # S = "abppplee"
    # W = "apple"
    # print(sol(S, W))
    #
    # S = "heat"
    # W = "hit"
    # print(sol(S, W))
    #
    S = "abppplee"
    W = "kangaroo"
    print(lcs(S, W))
    print(lcs_v1(S, W))


    S = "abppplee"
    D = ["able", "ale", "apple", "bale", "kangaroo"]
    print(sol(S, D))


else:
    #n, k = map(int, input().split())
    S =list( map(int, input().split()))
    k, a, b = S
    print(sol(k, a, b))


