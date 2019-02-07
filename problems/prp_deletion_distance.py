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
def longest_substring(str1, str2):
    ans = ""
    for p1 in range(len(str1)):
        is_seq = False
        tmp = ""
        for p2 in range(len(str2)):
            if str1[p1] == str2[p2]:
                print("m1: %s" % str1[p1])
                if is_seq:tmp += str1[p1]
                else: tmp = str1[p1]
                if len(tmp) > len(ans):ans = tmp
                is_seq = True
                p1+=1
                if p1 == len(str1): break
            else:
                is_seq = False
    return ans

def deletion_distance(str1, str2):
    sub = longest_substring(str1 if len(str1) <= len(str2) else str2, str2 if len(str1) <= len(str2) else str1)
    print("longest_substring: %s" % sub)
    sub_sz = len(sub)
    return len(str1) - sub_sz + len(str2) - sub_sz

# assert(deletion_distance("", "") == 0)
# assert(deletion_distance("dog", "frog") == 3)
# assert(deletion_distance("miso", "soup") == 4)
# assert(deletion_distance("school", "school") == 0)
# assert(deletion_distance("material", "atess") == 7)
# assert(deletion_distance("atess", "material") == 7)
assert(deletion_distance("heat", "hit") == 3)

# time: worstO(N*N),


"""
だめだ。
ヒントを見るまで解けなかった
これだとテストにheat, hitに引っかかる
"""