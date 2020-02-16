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


def findall(s, word):
    curr = s
    found = curr.find(word)
    A = []
    i = 0
    while found != -1:
        #print("i:%s, found:%s" % (i, found))
        A.append(found+i)
        i = i+found+1
        found = curr[i:].find(word)
        if found == -1: break

    return A

# print(findall("aaaaabbb", "a"))
# exit(0)
class Solution:
    def addBoldTag(self, s: str, D: List[str]) -> str:
        P = []
        for word in D:
            #i = s.find(word)
            Is = findall(s, word)
            for i in Is:
                if i != -1:
                    # found
                    P.append((i, i + len(word)-1))
            else:
                # not found
                pass
        P.sort(key=lambda tup: tup[0])
        print(P)
        A = []
        P.append((sys.maxsize, sys.maxsize))
        prev = None
        for (i, j) in P:
            # i: start
            # j: end (includsive)
            if prev == None:
                A.append(i)
            else:
                if i-1 <= prev and prev <= j:
                    pass
                elif j < prev:
                    continue
                else:
                    A.append(prev)
                    A.append(i)
            prev = j

        ans = ""
        print(A)
        A = A[:-1]
        print(A)
        # s = abcxyz123
        # P = [(0, 2) (6, 8)]
        A0 = { x:1 for i, x in enumerate(A) if i % 2 == 0} # start
        A1 = { x:1 for i, x in enumerate(A) if i % 2 == 1} # end
        print(A0)
        print(A1)
        for i in range(len(s)):
            if i in A0:
                ans += "<b>"
            ans += s[i]
            if i in A1:
                ans += "</b>"
        return ans


samples = [
    # (
    # "aaabbcc",
    # ["aaa","aab","bc","aaabbcc"]
    # ),
    (
        "aaabbcc",
        ["a","b","c"]
    )

]
for s, D in samples:
    ans = Solution().addBoldTag(s, D)
    print(ans)
