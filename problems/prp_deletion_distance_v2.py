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
cache = {}
def dd(str1, str2):
    if (str1, str2) in cache:
        #print("cache hit!")
        return cache[(str1, str2)]
    if str1 == str2:
        cache[(str1, str2)] = 0
        return 0
    if str1 == "" or str2 == "":
        cache[(str1, str2)] = max(len(str1), len(str2))
        return cache[(str1, str2)]
    if str1[-1] == str2[-1]:
        cache[(str1, str2)] = dd(str1[0:-1], str2[0:-1])
        return cache[(str1, str2)]
    else:
        cache[(str1, str2)] = 1 + min(dd(str1, str2[0:-1]), dd(str1[0:-1], str2))
        return cache[(str1, str2)]


def deletion_distance(str1, str2):
    return dd(str1, str2)

# assert(deletion_distance("", "") == 0)
# assert(deletion_distance("dog", "frog") == 3)
# assert(deletion_distance("miso", "soup") == 4)
# assert(deletion_distance("school", "school") == 0)
# assert(deletion_distance("material", "atess") == 7)
#assert(deletion_distance("atess", "material") == 7)
#print(deletion_distance("heat", "hit"))
#assert(deletion_distance("heat", "hit") == 3)

# time: worstO(N*N),


"""
だめだ。
ヒントを見るまで解けなかった
リカーシブ！！！
"""