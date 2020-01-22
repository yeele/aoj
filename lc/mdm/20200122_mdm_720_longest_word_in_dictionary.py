#https://leetcode.com/problems/word-ladder/discuss/473774/python-two-end-solution-100ms
from typing import List
from collections import defaultdict
import sys

def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

from collections import defaultdict
import time

class Trie:
    def __init__(self):
        self.db = {}

    def insert2(self, word: str) -> None:
        curr = self.db
        total_n_new_chars = 0
        for i, c in enumerate(word):
            if c in curr:
                if i == len(word) - 1: curr[c].update({"end":{}})
                else: curr[c].update({})
            else:
                if i == len(word) - 1:
                    curr[c] = {"end":{}}
                    return True
                else:
                    curr[c] = {}
                    return False
            curr = curr[c]
        return True
    def insert(self, word: str) -> None:
        curr = self.db
        for i, c in enumerate(word):
            if c in curr:
                if i == len(word) - 1: curr[c].update({"end":{}})
                else: curr[c].update({})
            else:
                if i == len(word) - 1: curr[c] = {"end":{}}
                else: curr[c] = {}
            curr = curr[c]

    def startsWith(self, prefix: str) -> bool:
        curr = self.db
        N = len(prefix)
        i = 0
        while i <= N and curr and prefix[i] in curr: # e in curr_db?
            if i == len(prefix) -1:
                return True
            curr = curr[prefix[i]]
            i+=1
        return False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        sorted_words = sorted(words)
        trie = Trie()
        import bisect
        A = []
        maxi = -sys.maxsize
        for word in sorted_words:
            if len(word[:-1]) == 0 or trie.startsWith(word[:-1]):
                trie.insert(word)
                if len(word) > maxi:
                    A = [] # reset
                    maxi = len(word)
                bisect.insort_left(A, word)
        A = [chars for chars in A if len(chars) == maxi]
        print(A, maxi)
        return A[0] if len(A) > 0 else None

samples = [
   ["a", "banana", "app", "appl", "ap", "apply", "apple"],
   ["w","wo","wor","worl", "world"],
   ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"],
   ["sg","qgca","s","qzu","qzub","qzubvs","hlyc","hl","qg","qzubv","qgc","qgcab","qz","sgs","sgsnyn","hly","hlycf","sgsn"]
]
for S in samples:
    ans = Solution().longestWord(S)
    print(ans)
