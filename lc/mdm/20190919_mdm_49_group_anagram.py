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

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            mp = defaultdict(int)
            for i in range(len(s)):
                mp[s[i]] += 1
            flatten = list(map(lambda kv : (kv[0], kv[1]), mp.items()))
            flatten.sort(key=lambda tp: tp[0])
            anagrams[str(flatten)].append(s)
        return anagrams.values()



samples = [
    # (
    #     ["eat", "tea", "tan", "ate", "nat", "bat"],
    #     [
    #         ["ate","eat","tea"],
    #         ["nat","tan"],
    #         ["bat"]
    #     ]
    # ),

    # 1713pm 実装5分ご最初の提出は, 47/101でこける。
    # wrong answer of me: [["eat"],["tea"],["tan"],["ate"],["nat"],["bat"]]
    # 1716pm 問題は、うまくdictのキーをstr西後きにソートされていないのが原因ですん。
    #        多分追加した順になっちゃんか。
    (
        ["eat","tea","tan","ate","nat","bat"],
        [["bat"],["nat","tan"],["ate","eat","tea"]]
    )
]

for S, expected in samples:
    ans = Solution().groupAnagrams(S)
    print(ans)


