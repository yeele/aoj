#-*- coding: utf-8 -*-
"""
ピボットソート実装してみます。
マージソート、とヒープソートが実装が楽だし
TOも効率的なのでおすすめです。
今回はpivotソートを実際に実装してみて、
なにが故に、tOがワーストでO(N^2)になるのか
sO(log(n))になるのか？がわかればいいかなと思います。
"""

S = [5, 4, 1, 8, 7, 2, 6, 3]


"""
最初に実装よりなんか汚くなっちったなー。
でもまぁ、それぞれの方法で実装できたからよし。
"""
class PivotSort():
    def __init__(self):
        self.gi = 0
    def sort(self, S):
        if len(S) <= 1:
            return S
        """
        対象のSが1だったら、ソート済とする。
        適当にpivotを選ぶ。
        ポインタl, rをセットする
        ポlを右にヅラして、S[pivot]より大きいが見つかるまで移動、見つからずに右ポ超えてもよし、右端に到達したら。
        ポrを左にヅラして、S[pivot]より小さいが見つかるまで移動、（すでに左マーカに抜けれている場合は右ポの移動はなく、=>
                                                             もし、左ポが右端に達している場合、pivotを操作済にして Fin
        1,見つかったら => swap l and r
        2,見つからずに右ポが左ポにぶつかる(一緒のindex)パターン => swap with pivot => l,r is Fin.
                        ---> l,rの位置にpivotが来ていて、その左と右のデータにわけることができ、これまでの操作を繰り返す。
        3,左ポが右ポを超えてpivotまで行くパターン
        これが実装できれば、pivotソートは終わりです。便宜上、pivotの選び方をランダムではなく右端に固定してみます。
        """
        def swap(S, i, j):
            tmp = S[i]; S[i] = S[j]; S[j] = tmp
        def _pivot_search(S, i, j):
            self.gi+=1
            if self.gi >= 1000: return
            "i start, j end,         l, r         p=pivot"
            if j - i == 0: return i
            p = j # pivot
            l = i
            r = p - 1
            while True:
                ii = 0
                while True:
                    ii+=1;
                    if ii>=1000:break;
                    print("(left) l:%s r:%s p:%s" % (l, r, p))
                    if S[l] > S[p]: break
                    if l >= j: break
                    l += 1
                ii=0
                while True:
                    ii+=1;
                    if ii>=1000:break;
                    print("(righta) l:%s r:%s p:%s" % (l, r, p))
                    if S[r] < S[p]: break
                    if r <= l: break
                    r -= 1
                if l < r:
                    swap(S, l, r)
                    l += 1; r -= 1
                elif l == r:
                    swap(S, l, p)
                    # lの位置のpivotが来ていてpivotは操作済！
                    _pivot_search(S, i, l-1)
                    _pivot_search(S, l+1, j)
                    break
                elif l == j:
                    # pivot is done 左ポが右端なので
                    _pivot_search(S, i, p-1)
                    _pivot_search(S, p+1, j)
                    break
            return S


        _pivot_search(S, i=0, j=len(S)-1)
        return S


print("Before merge S:%s" % S)
A = PivotSort().sort(S)
print("After merged A:%s" % A)