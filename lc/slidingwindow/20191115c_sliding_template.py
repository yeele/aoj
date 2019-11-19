#-*- coding: utf-8 -*-
from typing import List
import math

import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

import sys
sys.setrecursionlimit(314159265)

class Solution_my:
    def lengthOfLongestSubstring(self, S: str) -> int:
        if S is None or len(S) == 0: return 0
        sz = len(S)
        l = 0
        r = 1
        maxi = 1
        while l < sz and r < sz:
            #print("l -> %s, r -> %s" % (l, r))
            if S[r] in S[l:r]:
                # move l until  non overlap point
                while S[l] != S[r]:
                    l += 1
                l += 1
            else:
                maxi = max(maxi, r - l + 1)
                # move r +1
                r += 1


        return maxi


# let's
# write template in python first
# to get better understanding
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem
# then apply this into 3_longest_substring_without_repeating_characters

from typing import DefaultDict
from collections import defaultdict
class Solution():
    """
    これの肝は
    hmapで条件Tを管理すること
    counter:intで条件Tに違反したのでleft pointerをずらすフラグに利用
        さらに、counterとhmapでどこまでずらすかも管理
    することにある。
    擬似コード(pseudo code)はこんな。
    条件tによりhmap初期化(順列を構成する粒子で初期化)
    while 右ポが文字列より短い間
        右ポの文字をhmapから減らして、条件Tを判定
        違反していればcounterを++
        右ポをづらす　

        ポインターを使えるのは連続するという条件がはいっているから。
        （文字列という時点で連続ですし、その他、連続かどうかという点はダブルポインターがつかえるか
        　どうかの分かれ道ですね。使えない場合はdpになるんでしょうか。そんなぼんやり予想がありますが、
    　　　　今は先に進みます。）
        もし違反していればleft pointerを正しい位置までづらせないか考える。
        条件の違反がなくなるまで、ポインターをずらしつつ、かつ
        hmapへの進捗を巻き戻すよに。
        while　違反が溶けない限り:
            左ポの文字がhmapから外れるので、それを反映していく
            違反が解けたかどうか、それはcounter -= 1で表現
            左ポをづらす

        もし、文字列tが発見されたり、していれば
        答えを更新する

    """
    """
    と上の説明でこのテンプレートを細かく説明できたと思う。
    しかし、もっとハイレベルでキャッチーなテンプレートpseudo codeを説明しておきたい
    と思った。
    
    塊の中から条件Xをみたす連続値Tを探せ、という問題。
    
    条件Xが順列だったりするとhampが効果的。
    普通でも使えるので
    
    右ポをずらしながら、
    hmapで条件Xを判定します。
    条件内のときは右ポをづらしながら、
    条件からヅレた時は左ポを今度はズラします。
    左ポをずらしwhileではhmapでの進捗を違反が解けるまで巻き戻します。
    
    これが名付けて
    「hmap条件判定、連続値tをsliding window　検索アルゴリズム」です。
    
    
    """
    def solve_sliding_window(self, S: str, T: str):
        result: List[int] = []
        if len(T) > len(S): return result

        hmap: DefaultDict[str, int] = defaultdict(int)
        for s in S:
            hmap[s] += 1
        #print (hmap)
        counter = len(hmap)
        l = r = 0 # sliding window pointers

        while r < len(S):
            print("l:%s, r:%s, counter:%s, hmap:%s" % (l, r, counter, hmap))
            c = S[r]
            if c in hmap.keys():
                #--- business logic ---
                hmap[c] = hmap[c] - 1 # plus or minus one
                #modify the counter according the requirement(different condition).
                if hmap[c] == 0:
                    counter -= 1
                #--- business logic ---
            r += 1
            # l(left) pointerと管理変数をクリアするロジック
            while counter == 0: # depends on condition
                #--- business logic ---
                cl = S[l] # c(character) at left pointer
                if cl in hmap.keys():
                    hmap[cl] = hmap[cl] + 1
                    if hmap[cl] > 0:
                        counter += 1
                #--- business logic ---

                # save or update the result if find T
                # result = result
                l += 1
        return result



samples = [
    ("abcabcbb", 3),
    # ("bbbbb", 1),
    # ("pwwkew", 3),
]


for S, expected in samples:
    ans = Solution().solve_sliding_window(S, S)
    print(ans)