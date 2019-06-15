#-*- coding: utf-8 -*-
"""
Modify and return the given map as follows:
if the key "a" has a value, set the key "b" to have that same value.
In all cases remove the key "c", leaving the rest of the map unchanged.

mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
"""

# reverse S
# ans = 0
# seq = 0
# if digit . add up to ans
# if char is digit:
#   ans += int(char) * (10**i)
#   i++
# else: char is alphabet: seq = 0

def sol(D):
    for k in D.copy().keys():
        if k == "a":
            D["b"] = D["a"]
        elif k == "c":
            del D["c"]
    return D





import sys
sys.setrecursionlimit(314159265)
test = False
test = True
if test:
    testcases = [
        ({"a": "aaa", "b": "bbb", "c": "ccc"}, {"a": "aaa", "b": "aaa"})
        , ({"b": "xyz", "c": "ccc"}, {"b": "xyz"})
        ,({"a": "aaa", "c": "meh", "d": "hi"}, {"a": "aaa", "b": "aaa", "d": "hi"})
    ]
    # n, k = 5, 5
    #S =list( map(int, "4 2 6".split()))
    for case in testcases:
        D, e = case
        ret = sol(D)
        print(ret)
        #assert(ret == e)
else:
    #n, k = map(int, input().split())
    S =list( map(int, input().split()))
    k, a, b = S
    print(sol(k, a, b))


