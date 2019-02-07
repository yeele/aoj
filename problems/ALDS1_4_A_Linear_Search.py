#-*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A
Search I
You are given a sequence of n integers S and a sequence of different q integers T. Write a program which outputs C, the number of integers in T which are also in the set S.

Input
In the first line n is given. In the second line, n integers are given. In the third line q is given. Then, in the fourth line, q integers are given.

Output
Print C in a line.

Constraints
n ≤ 10000
q ≤ 500
0 ≤ an element in S ≤ 109
0 ≤ an element in T ≤ 109
"""
import random

# O(n^2)
def get_set(S, T):
    C = []
    for s in S:
        for t in T:
            if s == t: C.append(t)
    return C

# O(n^2) ??
def get_set2(S, T):
    return list(set(S).intersection(set(T)))

# O(log(n)) + O(n+q) = O(n)
def get_set3(S:list, T:list):
    D:dict = {}
    C = []
    for s in S:
        D[s] = 1
    for t in T:
        if t in D.keys() and D[t] == 1:
            D[t] = 2
            C.append(t)
    return C

def input_array():
    n = int(input())
    S = list(map(int, input().split()))
    return S

def input_from_txt():
    import requests
    url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_4_A/8/in"
    res = requests.get(url)
    input = res.text.split("\n")
    n = input[0]
    S = list(map(int, input[1].split()))
    q = input[2]
    T = list(map(int, input[3].split()))
    return (n, S, q, T)



if __name__ == '__main__':
    S = input_array()
    T = input_array()
    #(n, S, q, T) = input_from_txt()
    #print(n, S, q, T)
    ret = get_set3(S, T)
    print(len(set(ret)))
