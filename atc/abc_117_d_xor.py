#-*- coding: utf-8 -*-
"""
https://atcoder.jp/contests/abc117/tasks/abc117_a
"""

def sol_naive(k, S):
    maxi = 0
    for x in range(k+1):
        ttl = 0
        for s in S:
            ttl += (x ^ s)
        maxi = max(maxi, ttl)
    return maxi


def keta(x):
    if x <= 0:
        return 0
    else:
        return 1 + keta(int(x/2))

def bin(x):
    return "{0:08b}".format(x)

def rec(k, S, b_keta, ans): # which digit
    #print("rec(%s, %s, %s, %s)" % (k, S, b_keta, ans))
    if b_keta == 0:
        #print("miso")
        return ans
    else:
        #print("soup")
        ones = 0
        for s in S:
            #print("checking %s and %s" % (bin(s), bin(1 << (b_keta-1))))
            if (1 << (b_keta-1) & s) > 0:
                #print("it's 1")
                ones += 1
        if ones < len(S) - ones: # should be set 1 in this digit
            if ans + (1 << (b_keta-1)) <= k:
                ans += (1 << (b_keta-1))
            #print("ans updated %s" % ans)
            return rec(k, S, b_keta-1, ans)
        else:
            return rec(k, S, b_keta-1, ans)


def sol(k, S):
    maxi = max(S)
    b_keta = keta(k)
    #print("find maxi(%s) and it's digit is %s and k is (%s)" % (maxi, b_keta, k))
    x = rec(k, S, b_keta, 0)
    ans = 0
    for s in S:
        ans += (x ^ s)
    return ans

test = False
#test = True
if test:
    n, k = 3, 7
    S =list( map(int, "1 6 3".split()))
    print(sol(k, S))

    n, k = 4, 9
    S =list( map(int, "7 4 0 3".split()))
    print(sol(k, S))
    #
    n, k = 1, 0
    S =list( map(int, "1000000000000".split()))
    print(sol(k, S))


else:
    n, k = map(int, input().split())
    S =list( map(int, input().split()))
    print(sol(k, S))


