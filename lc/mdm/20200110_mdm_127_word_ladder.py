#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
from typing import List
from collections import defaultdict
import sys
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        counts = 1
        letters = 'abcdefghijklmnopqrstuvwxyz'
        if beginWord in wordList:
            wordList.remove(beginWord)
        word_dic = {i:1 for i in wordList} # for O(1) search
        l = set([beginWord])
        r = set([endWord])
        ll = set([beginWord]) # record all the words appeared
        #rr = set([endWord])

        while l:
            tmp = []
            for word in l:
                for ch in letters:
                    for i in range(len(word)):
                        new = word[:i]+ch+word[i+1:]
                        if (new not in ll) & (new in word_dic):
                            tmp.append(new)
            l = set(tmp)
            counts += 1
            ll = ll | l

            if l & r:
                return counts
            # これを入れたら動かんかったし、読んでいてもおかしいコード。だから外す。
            # if len(l) > len(r):
            #     l, r, ll, rr = r, l, rr, ll # for less branches


        return 0

ans = Solution().ladderLength(
"hit",
"cog",
["hot","dot","dog","lot","log","cog"]
)
print(ans)
