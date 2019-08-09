#-*- coding: utf-8 -*-
#https://leetcode.com/explore/interview/card/google/64/dynamic-programming-4/348/

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [[0] * (len(s)) for _ in range(len(s))]
        def get_dp(i, j, d):
            if i < 0 or i > len(dp): return d
            if j < 0 or j > len(dp): return d
            return dp[i][j]

        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j+1] in wordDict:
                    logging.info("hit on i%s, j%s :%s"%(i, j, s[i:j+1]))
                    sz = j+1-i
                    pi = i-sz+1
                    pj = j-sz
                    logging.info("pre i%s, j%s :%s" % (i, pj, get_dp(i, pj, 1)))

                    dp[i][j] = max(min(1, get_dp(i, pj, 1)), get_dp(i-1, j, 0))
                    if j == len(s)-1 and dp[i][j] == 1: return True
                else:
                    dp[i][j] = max(0, get_dp(i-1, j, 0))
        for a in dp:
            logging.info(a)
        return dp[-1][-1] == 1

s = "leetcode"; wordDict = ["leet", "code"]
#Explanation: Return true because "leetcode" can be segmented as "leet code".
s = "applepenapple"; wordDict = ["apple", "pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#Note that you are allowed to reuse a dictionary word.

s = "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
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