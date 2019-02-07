#-*- coding: utf-8 -*-
"""
【問題概要】
1 以上 N 以下の整数のうち、10 進法で各桁の和が A以上 B以下であるものについて、総和を求めてください。

【制約】

1≤N≤1041≤N≤104
1≤A≤B≤361≤A≤B≤36
入力はすべて整数
【数値例】
1)
　N=20
　A=2
　B=5
　答え: 84
20 以下の整数のうち、各桁の和が 2 以上 5 以下なのは、2, 3, 4, 5, 11, 12, 13, 14, 20 です。これらの合計である 84 を出力します
"""

import time
def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        func(*args, **kwargs)
        print('--end in %f --' % (time.time() - s) )
    return wrapper


from collections import defaultdict
dp = defaultdict(int)
def keta_total(x):
    if x in dp: return dp[x]
    if x == 0:
        dp[x] = 0
        return dp[x]
    else:
        dp[x] = (x % 10) + keta_total(int(x/10))
        return dp[x]

@deco
def sol(n, a, b):
    ttl = 0
    for x in range(n+1):
        tmp = keta_total(x)
        #print("keta_total(%s) = %s" % (x, tmp))
        if a <= tmp and tmp <= b:
            ttl += x

    return ttl



cases = [
    #500, 100, 50
    #(2, 2, 2, 100),
    #(2, 2, 8, 650),
    (10**4, 1, 36),
    (20, 2, 5)
]
for i, (S) in enumerate(cases):
    print("case%s: S:%s" % (i+1, S))
    n, a, b = S
    print(sol(n, a, b))


