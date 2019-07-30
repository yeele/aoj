# -*- coding: utf-8 -*-
from typing import List

"""
start @20190724 13:14
end   @20190724 14:56

Took 1.5 hour => 1st naive and notworking code 
"""

class Solution_BruteForce:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                # validation here, but O(n**2) bad solution
                r = 0
                for i, s in enumerate(S):
                    i += 1
                    if s == ')':
                        r += 1
                    if r > (i -r):
                        return
                    if (i-r) > n:
                        return
                res.append(S)
                return

            backtrack(S + '(', left + 1, right)
            backtrack(S + ')', left, right + 1)
        backtrack("", 0, 0)
        return list(set(res))

actual = Solution_BruteForce().generateParenthesis(3)
print("actual:%s" % actual)

class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                res.append(S)
                return

            if left < n:
                backtrack(S + '(', left + 1, right)
            if left > right:
                backtrack(S + ')', left, right + 1)
        backtrack("", 0, 0)
        return res

actual = Solution2().generateParenthesis(3)
print("actual:%s" % actual)






class Solution:
    def __init__(self):
        self.rets = set()
    def generateParenthesis(self, n: int) -> List[str]:
        ps = ['(', ')']
        l = ps[0]
        r = ps[1]
        pool = [l] * n + [r] * n
        #sprint(pool)
        self.rets = set()
        rets =  self.rec(pool, [], "")
        #print("finally rets => %s" % rets)
        return list(self.rets)

    def rec(self, pool=[], stack=[], chosen=""):
        if len(pool) == 0:
            status = self.validate(stack)
            if status == 0:
                #print("=> %s" % [chosen])
                self.rets.add(chosen)
                return [chosen]
            elif type(status) == str and len(status) > 0:
                #print("=> %s" % [chosen+status])
                self.rets.add(chosen+status)
                return [chosen+status]
            else:
                #print("=> nothing")
                return []
        else:
            rets = []
            for e in pool:
                pool_copied = pool[:]
                stack_copied = stack[:]
                pool_copied.remove(e)
                stack_copied.append(e)
                status = self.validate(stack_copied)
                if status == 0:
                    ret = self.rec(pool_copied, stack_copied, chosen)
                elif type(status) == str and len(status) > 0:
                    ret = self.rec(pool_copied, [], chosen+status)
                else:
                    return []
                rets += ret
                rets = list(set(rets))
            #print("current rets:%s" % rets)
            return rets

    def validate(self, stack):
        # return -1 if invalid, return 0 incomplete, return number of
        # parenthese if completed valid.
        from collections import defaultdict
        m = defaultdict(int)
        for e in stack:
            m[e] += 1
            if m[')'] > m['(']:
                return -1
        if m[')'] == m['('] and m[')'] > 0:
            return ''.join(stack)
        else:
            return 0

expected = [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

actual = Solution().generateParenthesis(3)
print("actual:%s" % actual)
#print(expected)
# assert(actual == expected, "should match!!")
