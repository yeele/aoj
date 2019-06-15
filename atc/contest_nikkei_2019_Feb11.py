#-*- coding: utf-8 -*-
"""
https://atcoder.jp/contests/abc117/tasks/abc117_a
"""
import math

def binary_1s(x):
    cnt = 0
    while x > 0:
        if x & 1: cnt += 1
        x = x >> 1
    return cnt

def binary_1s_index(x):
    cnt = 0
    i = 0
    indice = []
    while x > 0:
        if x & 1:
            indice.append(i)
        x = x >> 1
        i+=1
    return indice

def binary_all_one(keta):
    ans = 0
    for i in range(keta):
        ans |= (1 << i)
    return ans

def comb(S=[1, 2, 3], num=2):
    #0, 1, 2
    ans = []
    for i in range(binary_all_one(len(S))+1):
        #print('---')
        if binary_1s(i) == num:
            b1 = binary_1s(i)
            #print("{0:b}".format(i))
            indice = binary_1s_index(i)
            #print(indice)
            #print(S)
            ans.append( tuple([s for i, s in enumerate(S) if i in indice]) )
            #ans.append((S[indice[0]], S[indice[1]]))
            print(ans)
    return ans


def rec_prem(S, i, chosen, num):
    ans = []
    if 0 == len(S):
        return []
    elif len(chosen) == num:
        return [chosen]
    else:
        tmp = chosen.copy()
        tmp.append(S[i])
        tmpS = S.copy()
        del tmpS[i]
        ans += rec_prem(tmpS, i+1, tmp, num)
        ans += rec_prem(S, i+1, chosen, num)
        return ans


def prem(S, num=2):
    return rec_prem(S, 0, [], num)

prem([1, 3, 7, 11], 2)

def dist(A, B):
    x1, y1 = A
    x2, y2 = B
    return math.sqrt(abs(x1 - x2) + abs(y1 -y2))

def sol(N, XY):
    for pair in comb(XY):
        A, B = pair
        print (A, B, dist(A, B))
    return (N, XY)


test = False
test = True
if test:
    input_str = """4
    0 0
    5 0
    5 5
    0 5"""
    input_array = [x.strip() for x in input_str.split('\n')]
    N = input_array[0]
    XY = [ list(map(int, x.split())) for x in input_array[1:] ]

    print(sol(N, XY))


else:
    n, m = map(int, input().split())
    S =list( map(int, input().split()))
    #print(n, S)
    print(sol(n, S))


