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
    memo = [ [x for x in range(len(str2)+1)] for y in range(len(str1)+1)]

    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0: memo[i][j] = j
            elif j == 0: memo[i][j] = i
            elif str1[i-1] != str2[j-1]: memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])
            elif str1[i-1] == str2[j-1]: memo[i][j] = memo[i-1][j-1]
        #print("------")
        #for m in memo: print(*m)
    return memo[len(str1)][len(str2)]


# assert(deletion_distance("", "") == 0)
# assert(deletion_distance("dog", "frog") == 3)
# assert(deletion_distance("miso", "soup") == 4)
# assert(deletion_distance("school", "school") == 0)
# assert(deletion_distance("material", "atess") == 7)
#assert(deletion_distance("atess", "material") == 7)
#print(deletion_distance("heat", "hit"))
print(deletion_distance("atess", "material"))
#assert(deletion_distance("heat", "hit") == 3)
# time: worstO(N*N),


"""
だめだ。
ヒントを見るまで解けなかった
リカーシブ！！！
v２でヒント見て解けたけど、
v3で答えを見て、さらに動的プログラミングを
効率的に使っっている。と思って実装したが、実行速度は変わらなかった。
116msだった。対して、v2は110msだったので。 
"""