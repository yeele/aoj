#-*- coding: utf-8 -*-
"""
#https://www.pramp.com/challenge/61ojWAjLJbhob2nP2q1O
これは
prp_deletion_distance_v4_peer.pyに感化された。
彼はあの俺が難しいと思った問題を糸も簡単に
LCSの問題だと判断して、見事に動的プログラミングですぐといた
なので、今それを勉強、自分でメモとって復習した俺が数分で同じ問題を解けるかの確認です
開始時間：13:50pm 2018-12-26
"""


def lcs(str1, str2):

    dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0 or j == 0: dp[i][j] = 0
            elif str1[i-1] == str2[j-1]: dp[i][j] = 1 + max(dp[i-1][j], dp[i][j-1])
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

def delete_distance(str1, str2):
    return len(str1) + len(str2) - (2 * lcs(str1, str2))

str1 = "abcx"
str2 = "aybzc"
print(lcs(str1, str2))


str1 = "heat"
str2 = "hit"
print(delete_distance(str1, str2))