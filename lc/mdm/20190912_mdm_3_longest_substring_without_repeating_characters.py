#Definition for singly-linked list.

def timeit(method):
    def timed(*args, **kw):
        global calc
        calc = defaultdict(int)
        print ('===========')
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.8f ms' % (method.__name__, (te - ts) * 1000))
        print("calc %s times" % sum(calc.values()))
        return result
    return timed


from typing import List
import sys
import logging
import itertools
from collections import defaultdict
import time
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
from collections import defaultdict
class Solution:
    """
    何度もデバッガーをつかって20分ほどで
    ようやく正解にたどりつく。思考よりもデバッガと試行をくりかえして解いたので
    本番では、コツやここから得られるものをペーパーで
    できなくてはならない。
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # remember last index
        # if same char, curr - last index.
        # update the maxi all the time
        # O(n) algorithm
        memo = defaultdict(lambda : -1)
        maxi = 0
        j = -1
        for i, c in enumerate(s):
            if memo[c] >= 0: # already exist
                if j > memo[c]:
                    cur = i - j + 1
                else:
                    cur = i - memo[c]
                maxi = max(maxi, cur)
                j = max(j, memo[c] + 1)
            else:
                extra = 1 if j >= 0 and s[j] != s[i] else 0
                maxi = max(maxi, i-j+extra)
            memo[c] = i
        return maxi



class Solution_kaisetsu:
    """
    何度もデバッガーをつかって20分ほどで
    ようやく正解にたどりつく。思考よりもデバッガと試行をくりかえして解いたので
    本番では、コツやここから得られるものをペーパーで
    できなくてはならない。
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # remember last index
        # if same char, curr - last index.
        # update the maxi all the time
        # O(n) algorithm
        memo = defaultdict(lambda : -1)
        maxi = 0
        j = -1
        for i, c in enumerate(s):
            if memo[c] >= 0: # already exist
                if j > memo[c]:
                    cur = i - j + 1
                else:
                    cur = i - memo[c]
                maxi = max(maxi, cur)
                j = max(j, memo[c] + 1)  # j(開始ポイント)の更新！！
            else:
                extra = 1 if j >= 0 and s[j] != s[i] else 0
                maxi = max(maxi, i-j+extra)
            memo[c] = i                  # インデックスの更新
        return maxi

        # 終わってみれば、開始ポイントの更新がキーポイントである。
        # 素直に自分の前のインデックスに戻るパターンか、それ以後にくるduplicated　文字のインデックス化
        #   ==> これを抽象化すれば、最後のduplicated文字のindexさえ、追っていればよいのではないか！？
        #       ==> 

samples = [
    ( "abcabcbb", 3 ),
    ( "bbbbb", 1 ),
    ( "pwwkew", 3),
    ( "abcca", 3 ),
    ( "abccadacbbb", 4 ),
    ( "aab", 2 ),
]

for S, expected in samples:
    ans = Solution().lengthOfLongestSubstring(S)
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))

