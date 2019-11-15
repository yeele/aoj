#-*- coding: utf-8 -*-
from typing import List
import math

import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

import sys
sys.setrecursionlimit(314159265)

# copy and paste
#https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/423408/python3-99-runtime-100-memory
from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        solu = []
        word_map = defaultdict(int)
        if len(s) == 0 or len(words) == 0:
            return solu
        for word in words:
            word_map[word] += 1
        print(word_map)

        length = len(words[0])  # length of any word
        for i in range(0, length):
            start = i
            count = 0
            curr_word_map = defaultdict(int)

            for j in range(start, len(s)-length+1, length):
                subword = s[j:j+length]

                # check if the subword exists in the map
                if subword in word_map:
                    curr_word_map[subword] += 1
                    count += 1
                    #print("found:", subword)
                    #print("current dict:", curr_word_map)

                    # if current word count of some word is larger than
                    # that of actual num of words, reduce count and move
                    # start pointer one length further
                    while(curr_word_map[subword] > word_map[subword]):
                        removed = s[start:start+length]
                        #print("removing:", removed)
                        curr_word_map[removed] -= 1
                        start += length
                        count -= 1
                    # if all words have been counted in this sequence, add
                    # the answer to result
                    if count == len(words):
                        solu.append(start)
                        # then we move one word length further and continue our
                        # search
                        removed = s[start:start+length]
                        curr_word_map[removed] -= 1
                        start += length
                        count -= 1
                        #print("adding solu", start)

                else:
                    count = 0
                    start = j + length
                    curr_word_map.clear()
        return solu


samples = [
    ("barfoothefoobarman", ["foo","bar"], [0,9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    # 113/147 failed
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
    #  79/147 failed and degreade...
    ("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"], [13]),
    # 148 / 173  failed by TLE
    # that's it for now.
]


for S, words, expected in samples:
    ans = Solution().findSubstring(S, words)
    print(ans)

