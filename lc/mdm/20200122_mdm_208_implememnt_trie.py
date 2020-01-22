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

    def search(self, word: str) -> bool: # eve
        curr = self.db
        N = len(word)
        i = 0
        while i < N and curr and word[i] in curr: # N=2, curr = {...}, e in
            if i == len(word) -1 and "end" in curr[word[i]]:
                return True
            curr = curr[word[i]]
            i+=1
        return False

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


# Your Trie object will be instantiated and called as such:
trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))   # returns true
print(trie.search("app"))     # returns false
print(trie.startsWith("app")) # returns true
print(trie.insert("app"))
print(trie.search("app"))     # returns true