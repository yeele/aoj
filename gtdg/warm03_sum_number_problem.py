#-*- coding: utf-8 -*-
"""
Given a string, return the sum of the numbers appearing in the string,
ignoring all other characters.
A number is a series of 1 or more digit chars in a row.
(Note: Character.isDigit(char) tests if a char is
one of the chars '0', '1', .. '9'. Integer.parseInt(string)
converts a string to an int.)

sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
"""

# reverse S
# ans = 0
# seq = 0
# if digit . add up to ans
# if char is digit:
#   ans += int(char) * (10**i)
#   i++
# else: char is alphabet: seq = 0

def sol(S):
    #print(S, len(S))
    ans = place = 0
    for i in range(len(S)-1, -1, -1):
        s = S[i]
        if s.isdigit():
            ans += int(s) * (10**place)
            place += 1
        else:
            place = 0
    return ans




import sys
sys.setrecursionlimit(314159265)
test = False
test = True
if test:
    testcases = [
        ("abc123xyz", 123)
        ,("aa11b33", 44)
        ,("7 11", 18)
    ]
    # n, k = 5, 5
    #S =list( map(int, "4 2 6".split()))
    for case in testcases:
        S, e = case
        ret = sol(S)
        print(ret)
        #assert(ret == e)
else:
    #n, k = map(int, input().split())
    S =list( map(int, input().split()))
    k, a, b = S
    print(sol(k, a, b))


