"""
Question: Given a stack, sort the elements in the stack using one additional stack.
eg.
sort([1, 3, 2, 4]) = [1, 2, 3, 4]
Solution: https://www.byte-by-byte.com/sortstacks/
"""

"""
bubble, selection, insertion sO(1)
Merge sort -> recursion and stack(logN) + 1 stack
Quick sort ->  
"""

def quicksort(S):
    """
    [1, 3, 9, 2]
           p
    ピボットわすれた。。。
    どうやったら思い出せるかな。

    対象のSが1だったら、ソート済とする。 適当にpivotを選ぶ。
     ポインタl, rをセットする ポlを右にヅラして、
     S[pivot]より大きいが見つかるまで移動、見つからずに右ポ超えてもよし、
     右端に到達したら。
     ポrを左にヅラして、S[pivot]より小さいが見つかるまで移動、
     （すでに左マーカに抜けれている場合は右ポの移動はなく、=>
     もし、左ポが右端に達している場合、pivotを操作済にして
     Fin 1,見つかったら => swap l and r 2,
     見つからずに右ポが左ポにぶつかる(一緒のindex)パターン =>
      swap with pivot => l,r is Fin.
      ---> l,rの位置にpivotが来ていて、
      その左と右のデータにわけることができ、これまでの操作を繰り返す。
      3,左ポが右ポを超えてpivotまで行くパターン これが実装できれば、
    pivotソートは終わりです。
    便宜上、pivotの選び方をランダムではなく右端に固定してみます。
    """

    """
    もう一度まっさらな頭で考えたい
    
    なので
    lとrを両端におく
    pを適当に選ぶ
    sorted_indice = [] というバッファを持っておく
    
    l を　右->方向に 走査
      S[l] > S[p]があれば止まる
      もしくはrまで達すると止まる
    r を　左<-方向に 走査
      S[l] < S[p]があれば止まる
      もしくは左にであうと止まる
      しかしすでに左が左にない場合は、終わり
    if l < rなら、l と r　をスワップする
    か
    lrが同じ位置なら lrとpをスワップ
    このあと、recursiveに頑張れ!
    
    """
    def sort(S, i, j): # [1, 3, 9, 2], 0, 3
        #print(i, j)
        if i >= j: return
        # my join is partition i to j (inclusive)
        p = (j - i) // 2  #  1
        """
        [1, 3, 9, 2]
         i     j
        """
        while i <= j: # 0 <= 3
            while True:
                if S[i] > S[p]: break
                if i == j: break
                i += 1
            while i < j:
                if S[j] <= S[p]: break
                if i == j: break
                j -= 1
            if i < j:
                S[i], S[j] = S[j], S[i]
                i+=1; j-=1
            elif i == j:
                S[i], S[p] = S[p], S[i]
                break
            else:
                break
        sort(S, i, p-1)
        sort(S, p+1, j)

    sort(S, 0, len(S)-1)
    return S

print(quicksort([1, 3, 9, 2]))
print(quicksort([1, -3, 9, 0, 2, 1]))


# https://www.youtube.com/watch?v=uXBnyYuwPe8
# quicksort

# pivot
# partition


"""
p = choose_pivot
partition(S, i, j, p)

3 7 8 2 1
i (last insertion point)
j (scan)

3 7 8 2 1
i 
  j 
"""

def pivot(i, j):
    return (j - 1) // 2 + i

def qsort(S, i, j):
    def partition(S, s, e, p):
        if e - s <= 1:
            return S
        i, j = 0, 0
        while j <= e:
            #pivotより小さければiに彫り込む
            if S[j] < S[p]:
                if i == j:
                    j += 1
                else:
                    S[i], S[j] = S[j], S[i]
                    i += 1
                    j += 1
            else:
                j += 1
        return S

    p = pivot(i, j)
    if i <= p <= j:
        partition(S, i, j, p)
        qsort(S, i, p-1)
        qsort(S, p+1, j)
    return S

print(qsort([1, 3, 9, 2], 0, 3))
print(qsort([1, -3, 9, 0, 2, 1], 0, 5))

"""
# Worstcase O(N^2)
        p      
3 7 8 2 1
i      
      j
Swap p <-> i

p             
1 7 8 2 3
  i      
      j


  p            
3 7 8 2 1
i      
j

# 最初にpivotは右端に退避させて
          p
8 4 5 8 9 6
i        
j

pivotのベスト洗濯は中央値
iはpivotより小さい数を見つけた時のポインター
最終的に

      p    
4 5 8 6 9 7
    i        
          j



"""


def partition(S, s, e, p):
    if e - s <= 1:
        return S
    i, j = s, s
    if S[i] == S[p]: i += 1
    while j <= e:
        #pivotより小さければiに彫り込む
        if S[j] < S[p]:
            S[i], S[j] = S[j], S[i]
            i += 1
            j += 1
        else:
            j += 1
    if p < i:
        S[i-1], S[p] = S[p], S[i-1]
    else:
        S[i], S[p] = S[p], S[i-1]
    return S

print("--- test partition ---")
S = [3, 7, 8, 2, 1]
print(partition(S, 0, len(S)-1, 2))
print(partition(S, 0, len(S)-1, 0))

S = [3, 7, 8, 2, 1]
print(partition(S, 0, len(S)-1, 2))
print(partition(S, 0, len(S)-1, 0))


S = [1, -3, 9, 0, 2, 1]
print(partition(S, 0, len(S)-1, 3))