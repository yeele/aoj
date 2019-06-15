#-*- coding: utf-8 -*-
"""
https://yahoo-procon2019-qual.contest.atcoder.jp/tasks/yahoo_procon2019_qual_a
"""

from collections import defaultdict
dp = defaultdict(int)
def rec(l, k, bis, y, a, b):
    print(l, k, bis, y, a, b)
    if (l, bis, y) in dp:
        print("hit, dp size %s" % len(dp))
        return dp[(l, bis, y)]
    if l == k+1:
        dp[(l, bis, y)] = bis
        return bis
    else:

        if y > 0: ret = rec(l+1, k, bis+b, y-1, a, b)
        elif bis >= a: ret = rec(l+1, k, bis-a, y+1, a, b)
        else: ret = rec(l+1, k, bis+1, y, a, b)
        dp[(l, bis, y)] = ret
        return dp[(l, bis, y)]

def sol_botsu(k, a, b):
    # global dp
    # dp = defaultdict(int)
    # return rec(1, k, 1, 0, a, b)
    bis = 1
    y = 0
    for i in range(k):
        if y > 0: bis+=b; y-=1
        elif bis >= a: bis-=a; y+=1
        else: bis+=1
    return bis

def sol_botsu2(k, a, b):
    bis = 1
    y = 0
    i = 0
    while k > 0:
        print(k, bis, y)
        rest = a - (bis % a)
        if k - (rest) >= 2:
            print("saving")
            k-=(rest); y+=1; bis-=(bis % a); k-=1;
        elif y > 0:
            print("payoff")
            k -= 1; bis = (y*b); y = 0;
        else:
            print("normal")
            if k > a:
                k-=a; bis += a
            else:
                bis += k; k = 0
        i+=1
        #if i == 20: break
    return bis


def sol_botsu3(k, a, b): # なぜに！？
    print(k, a, b)
    bis = 1
    bank = 0
    y = 0
    i = 1
    while k > 0:
        print("status:i:%s, k:%s, bis:%s y:%s, bank:%s" % (i, k, bis, y, bank))
        need = a - (bis % a)
        if k - (need) >= 2:
            print("saving")
            k-=(need); bis+=need
        elif k -1 >=1 and bis >= a:
            print("buying yen")
            x = (bis/a)
            k-=1; y+=x; bis-=(a*x);
        elif y > 0:
            print("pay off")
            k-=1; bank += y*b; y = 0
        else:
            #print("unexpected")
            print("finishing")
            bis += k; k=0;
            #k-=1; bis+=1;
        i+=1
    return bank + bis


def sol_botsu4(k, a, b):
    print(k, a, b)
    bis = 1
    bank = 0
    y = 0
    i = 1
    while k > 0:
        print("status:i:%s, k:%s, bis:%s y:%s, bank:%s" % (i, k, bis, y, bank))
        need = a - (bis % a)
        if y == 1:
            #print("Y -> bis")
            k-=1; bank += y*b; y = 0
        elif y == 1:
            #print("Y -> bis(unexpected)")
            k-=1; bank += y*b; y = 0
        elif k -1 >=1 and bis >= a:
            x = (bis/a)
            #print("bis -> Y(buying %s Y by bis:%s" % (x, bis))
            k-=1; y+=x; bis-=(a*x);
        elif k - (need) >= 2:
            #print("progress %s to increase bis" % need)
            k-=(need); bis+=need
        else:
            #print("kotsukotsu")
            k-=1; bis+=1



        i+=1
    return bank + bis



def sol(k, a, b):
    bis = 1
    if 1+k < a:
        return k+1
    else:
        bis += int((k-1)/2) * (b-a)
        if k % 2 == 1:
            bis += 1
        return bis



import sys
sys.setrecursionlimit(314159265)
test = False
test = True
if test:
    # n, k = 5, 5
    S =list( map(int, "4 2 6".split()))
    k, a, b = S
    print(sol(k, a, b))

    S =list( map(int, "7 3 4".split()))
    k, a, b = S
    print(sol(k, a, b))

    S =list( map(int, "314159265 35897932 384626433".split()))
    # 48518828981938099
    k, a, b = S
    print(sol(k, a, b))


else:
    #n, k = map(int, input().split())
    S =list( map(int, input().split()))
    k, a, b = S
    print(sol(k, a, b))


