#-*- coding: utf-8 -*-
"""
https://www.youtube.com/watch?v=Cl9U027Rb9s&index=15&list=PLnfg8b9vdpLn9exZweTJx44CII1bYczuk
"""


"""
以下の方法はバックトラッキングではなく
単純な再起だ

なぜかというと、配列を毎回、コピーしてパラメータに渡している
これは、メモリーの食う

それを止めるためにレフェレンスを送るとする、
その場合、chosen.append(1)
として　chosenを引数に渡すわけだが、この場合、
戻ってきたときに、選んだchose.append(1)を
元に戻す( this is why, it's called backtracking)
必要がある
chosen[0:-1].append(2)
rec(n-1 chose)みたいな
"""
def rec(n, chosen):
    #print("rec(%s, %s)" % (n, chosen))
    #if len(chosen) == n:
    if n == 0:
        #if sum(chosen)==4:
        logging.info(chosen)
    else:
        rec(n-1, chosen+[1])
        rec(n-1, chosen+[2])
        rec(n-1, chosen+[3])
        rec(n-1, chosen+[4])
        rec(n-1, chosen+[5])
        rec(n-1, chosen+[6])

def sol(n):
    return rec(n, [])

import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")


ret = sol(3)
logging.info(ret)