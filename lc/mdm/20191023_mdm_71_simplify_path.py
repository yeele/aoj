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
from collections import defaultdict

class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = []
        for element in path.split('/'):
            if element == '' or element == '.':
                pass
            elif element == "..":
                if len(canonical) > 0:
                    canonical.pop()
            else:
                canonical.append(element)
        return "/" + "/".join(canonical)




samples = [
    ( "/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ( "/a/./b/../../c/", "/c"),
    ("/a/../../b/../c//.//", "/c"),
    ("/a//b////c/d//././/..", "/a/b/c"),
]

for S, expected in samples:
    ans = Solution().simplifyPath(S)
    print(ans)
