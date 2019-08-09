#-*- coding: utf-8 -*-
#https://leetcode.com/explore/interview/card/google/64/dynamic-programming-4/348/

class Solution:
    def wordBreak(self, S, words):
        dp = [ [1]+([0]*len(S)) for _ in range(len(S)+1)]

        for i in range(1, len(S)+1):
            for j in range(1, len(S)+1):
                #dp[i][j] = 1
                print("checking S[i-1:j]:%s" % S[i-1:j])
                if S[i-1:j] in words:
                    word_sz = j - i + 1
                    print("%s (%s) in words" % (S[i-1:j], word_sz))
                    dp[i][j] = dp[i][j - word_sz]
                else:
                    dp[i][j] = dp[i-1][j]

        for row in dp:
            print(row)
        return dp[-1][-1]


s = "leetcode"; wordDict = ["leet", "code"]
#Explanation: Return true because "leetcode" can be segmented as "leet code".
s = "applepenapple"; wordDict = ["apple", "pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#Note that you are allowed to reuse a dictionary word.

#s = "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
#Output: false
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.WARN, format="%(message)s")
# s = "leetcode"; wordDict = ["leet", "code"]
# print(Solution().wordBreak(s, wordDict))
# s = "applepenapple"; wordDict = ["apple", "pen"]
# print(Solution().wordBreak(s, wordDict))
# s = "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))

#print(Solution().wordBreak("aaaaaaa", ["aaaa","aaa"]))