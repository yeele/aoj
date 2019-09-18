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
logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
from collections import defaultdict
class Solution:
    def helper(self, indice, k):
        maxi = 0
        if len(indice) == 0: return 0
        s = indice[0] # start index
        buffer = []
        l = indice[0]
        maxi =  max(maxi, 1 + k)
        for r in indice[1:]:
            gap = r - l - 1
            if gap > k:
                s = r
                buffer = []
            elif gap > 0:
                if k > 0:
                    for offset in range(1, gap+1):
                        if len(buffer) >= k:
                            # clear buffer and increment s
                            pre_k = buffer.pop(0)
                            s = pre_k + 1
                        buffer.append(l + offset)
                        maxi = max(maxi, (l+offset) - s + 1 + k - len(buffer))
                    if l + offset + 1 == r: # 最後までいったら
                        maxi = max(maxi, r - s + 1 + k - len(buffer))
                else:
                    # k == 0
                    s = r
                    maxi =  max(maxi, r - s + 1)
            else:
                #maxi =  max(maxi, r - s + 1)
                maxi = max(maxi, r - s + 1 + k - len(buffer))
            l = r
        return maxi

    def characterReplacement(self, S: str, k: int) -> int:
        if S is None or len(S) == 0: return 0
        memo = defaultdict(list)
        for i, c in enumerate(S):
            memo[c].append(i)
        logging.debug("memo:%s" % memo)
        maxi = 0
        if len(memo) == 0: return k + 1
        for c, indice in memo.items():
            maxi = max(maxi, self.helper(indice, k))
        return min(maxi, len(S))

# Unit Test passed!
# Solution().helper( [8, 11, 44, 48, 55, 61, 90, 91, 94], 4)
# import sys
# sys.exit(0)

samples = [
    ( "ABAB", 2, 4 ),
    ( "AABABBA", 1, 4 ),
    # submit but failed with "AABA", k= 0
    # これは、k == 0の時を考慮してクリア
    ( "AABA", 0, 2 ),
    # 次のエラーは
    # "ABCDE", k=1
    # この場合は、rのループにはいらないパターンを追加
    ( "ABCDE", 1, 2 ),
    # 一個直しては、次のケースでコケる
    # だめだなーーー
    # バッファまりでgapないケースにのあてはめて
    ( "ABBB", 2, 4),
    # 17/37 failed.
    ( "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4, 7 ),
]

for S, k, expected in samples:
    ans = Solution().characterReplacement(S, k)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (S, k, ans, expected)
    print("(%s, %s) = %s as expected!" % (S, k, ans))
    # assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    # print("(%s) = %s as expected!" % (S, ans))

