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



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        memo = defaultdict(int)
        for word in words:
            memo[word] += 1

        topn = [(n, word) for word, n in memo.items()]
        topn.sort(key = lambda tp: (-tp[0], tp[1]))
        #print(topn)
        return [word for n, word in topn[:k]]


samples = [
    (
        ["i", "love", "leetcode", "i", "love", "coding"], 2,
        ["i", "love"]
    ),
    (
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4,
        ["the", "is", "sunny", "day"]
    )

]
for S, k, e in samples:
    ans = Solution().topKFrequent(S, k)
    print(ans)
