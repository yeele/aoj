#-*- coding: utf-8 -*-
"""
NN 枚のカードがあり、ii 枚目のカードには aiai という数が書かれています。
Alice と Bob はこれらのカードを使ってゲームを行います。ゲームでは 2 人が交互に 1 枚ずつカードを取っていきます。Alice が先にカードを取ります。
2 人がすべてのカードを取ったときゲームは終了し、取ったカードの数の合計がその人の得点になります。2 人とも自分の得点を最大化するように最適戦略をとったとき、Alice は Bob より何点多くの得点を獲得できるかを求めてください。
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

from collections import defaultdict
@deco
def sol(S):
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    return len(list(d.keys()))






cases = [
    (8,10,8,6)
]
for i, (S) in enumerate(cases):
    print("case%s: S:%s" % (i+1, S))
    A = S
    print(sol(A))


