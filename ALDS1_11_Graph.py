#-*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A
"""
import itertools


def input_from_txt(number=1):
    import requests
    #url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_4_A/8/in"
    url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_11_A/%s/in" % number
    res = requests.get(url)
    input = res.text.split("\n")
    n = int(input[0])
    Ss = []
    for i in range(n):
        S = list(map(int, input[1+i].split()))
        Ss.append(S)
    return (n, Ss)

def input_array():
    n = int(input())
    Ss = []
    for i in range(n):
        S = list(map(int, input().split()))
        Ss.append(S)
    return (n, Ss)


if __name__ == '__main__':
    (n, Ss) = input_array()
    #(n, Ss) = input_from_txt(1)
    #print(n, Ss)
    for i in range(n):
        vth = Ss[i][0]
        vd = Ss[i][1]
        adjs = Ss[i][2:]
        row = []
        for j in range(1, 1+n):
            if j in adjs: row.append(1)
            else: row.append(0)
        print(" ".join(map(str, row)))
    #ret = get_set4(S, T)
    #ret = get_set2(S, T)
    #ret = get_set(S, T)
    #print(len(ret))
