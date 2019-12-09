#-*- coding: utf-8 -*-
"""
https://www.coursera.org/learn/algorithms-divide-conquer/lecture/4vzQr/merge-sort-motivation-and-example

この問題は
まーじそーとを実際に実装してみてくれる！？
って言われても、できる、という自信につながりました。
これ自体は、何も見ずにに10分くらいで動くものができた。
自分が成長しているという証でもあり嬉しい。@20190710
"""

S = [5, 4, 1, 8, 7, 2, 6, 3]


"""
最初に実装よりなんか汚くなっちったなー。
でもまぁ、それぞれの方法で実装できたからよし。
"""
def merge_sort(S):
    if len(S) <= 1:
        return S
    else:
        m = int(len(S)/2)
        A = merge_sort(S[:m])
        B = merge_sort(S[m:])
        Q = []
        i = j = 0
        for k in range(len(S)):
            if i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    Q.append(A[i])
                    i+=1
                else:
                    Q.append(B[j])
                    j+=1
            elif i >= len(A) and j < len(B):
                Q.append(B[j])
                j+=1
            elif j >= len(B) and i < len(A):
                Q.append(A[i])
                i+=1
            else:
                assert(True, "don't come here")
        return Q


"""
これ自体は悪くないんだけど、whileループがなんとも
複雑だ。事業ではもっとシンプルだったのでそちらの実装を上ですr。
"""
def merge_sort_NotBad(S):
    if len(S) <= 1:
        return S
    else:
        m = int(len(S)/2)
        A = merge_sort(S[:m])
        B = merge_sort(S[m:])
        Q = []
        while A or B:
            if len(A) > 0 and len(B) > 0:
                if A[0] <= B[0]:
                    Q.append(A.pop(0))
                else:
                    Q.append(B.pop(0))
            elif len(A) > 0 and len(B) == 0:
                Q.append(A.pop(0))
            elif len(B) > 0 and len(A) == 0:
                Q.append(B.pop(0))
            else:
                assert(True, "don't come here")
        return Q



print("Before merge S:%s" % S)
A = merge_sort(S)
print("After merged A:%s" % A)