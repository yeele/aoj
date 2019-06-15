#-*- coding: utf-8 -*-
"""
"""

import time
def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        #print('--start--')
        ret = func(*args, **kwargs)
        print('--end in %f --' % (time.time() - s) )
        return ret
    return wrapper



"""
misosoup
miso
i
    i
i = 0, len(miso) = 4
0 + 4 = 4. now i = 4

i = 4, len(abc) = 3
i = 7
misosoup
    i
       i    
"""
@deco
def sol_notworking(s, T):
    ans = ""
    i = 0 # pointer
    while len(ans) < len(s):
        x = 0
        # which is the best
        # x ????
        if s[i] == "d":
            if len(s)-1 >= i + 5 and s[i+5] == "r":
                x = 0
            elif len(s)-1 >= i + 5 and s[i+5] == "":
                pass
        elif s[i] == "e": pass
        else: return False
        ans += T[x]
        i += len(T[x])
        if ans == s: return True
    return ans == s


def rec(s, T, i, chopped):
    if len(chopped) == 0:
        return True
    else:
        return any([
            rec(s, T, i+len(t), s[i+len(t):])
            for t in T
            if chopped.startswith(t)
        ])


@deco
def sol_rec(s, T):
    return rec(s, T, 0, s[:])


# solution by dp
@deco
def sol(s, T):
    dp = [0] * (len(s)*2)
    dp[0] = 1
    for i, c in enumerate(s):
        for t in T:
            if dp[i] == 1 and s[i:].startswith(t):
                dp[i+len(t)] = 1
    return dp[len(s)] == 1

from collections import defaultdict
import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

cases = [
    #(9, 45000),
    ("dreameraser", ("dream", "dreamer", "erase", "eraser")),
    ("dreamraser", ("dream", "dreamer", "erase", "eraser")),
    ("dreameraser", ("dream", "dreamer", "erase", "eraser")),
    ("dreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraserdreameraser", ("dream", "dreamer", "erase", "eraser"))
]
for i, (S) in enumerate(cases):
    print("case%s: S:%s" % (i+1, S))
    s, T = S
    print(sol(s, T))
    print(sol_rec(s, T))


