#-*- coding: utf-8 -*-
"""
https://techdevguide.withgoogle.com/paths/foundational/sequence-2/stringsplosion-problem-ccocodcode#!
https://codingbat.com/prob/p118366


Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""



def sol(S):
    ans = ""
    for i in range(1, len(S)+1):
        for j in range(i):
            ans += S[j]
    return ans



import sys
sys.setrecursionlimit(314159265)
test = False
test = True
if test:
    # n, k = 5, 5
    #S =list( map(int, "4 2 6".split()))
    S = "Code"
    print(sol(S))

    S = "abc"
    print(sol(S))

    S = "ab"
    print(sol(S))


else:
    #n, k = map(int, input().split())
    S =list( map(int, input().split()))
    k, a, b = S
    print(sol(k, a, b))


