#-*- coding: utf-8 -*-
"""
https://www.pramp.com/challenge/61ojWAjLJbhob2nP2q1O
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer
"""

def deletion_distance(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    ans = [[0]*(l2+1) for _ in range(l1+1)]
    for i1, ch1 in enumerate(str1):
        for i2, ch2 in enumerate(str2):
            if ch1 == ch2:
                ans[i1+1][i2+1] = 1 + ans[i1][i2]
            else:
                ans[i1+1][i2+1] = max(ans[i1][i2+1], ans[i1+1][i2])
    match_len = ans[-1][-1]
    return l1 + l2 - 2 * match_len





def deletion_distance_LESS_Dynamic_Memory(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    ans = [0]*(l2+1)
    for i1, ch1 in enumerate(str1):
        next_ans = [0]*(l2+1)
        for i2, ch2 in enumerate(str2):
            if ch1 == ch2:
                next_ans[i2+1] = 1 + ans[i2]
            else:
                next_ans[i2+1] = max(ans[i2+1], next_ans[i2])
        ans = next_ans
    match_len = ans[-1]
    return l1 + l2 - 2 * match_len

str1 = "dog"
str2 = "frog"
print (deletion_distance(str1, str2))

"""
だめだ。
Wed, Dec 26th 2018, 09:00 AM
受けた相手
やばい、
速い。。。
自信なくしたぜ。
なぜ、８時間前にこの問題、似たやつといたよって
言っていたんだが、 
"""