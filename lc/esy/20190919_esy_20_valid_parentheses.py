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

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "": return True
        OPEN = ['(', '[', '{'] # ideally use char code
        stack = []
        for c in s:
            if c in OPEN:
                stack.append(c)
            else:
                if len(stack) == 0: return False
                o = stack.pop()
                if o == '(' and c == ')': pass
                elif o == '[' and c == ']': pass
                elif o == '{' and c == '}': pass
                else: return False
        # through to end and no stack left => True
        return len(stack) == 0



samples = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("({(())})", True),
    ("({(()))}", False),
    ("({(()))}", False),

]

for s, expected in samples:
    ans = Solution().isValid(s)
    print(ans)


