#-*- coding: utf-8 -*-
"""
https://leetcode.com/problems/two-sum/description/
"""

"""
再起で、リストを返して最終的な回答が
リストのリストにするには、リストのリストを返す
この部分ね！[ret]
retはリストなので、
ret = ["ball", "area"]
[ret] = [["ball", "area"]] こういう感じになります！いえい！！
https://stackoverflow.com/questions/50376764/returning-a-list-of-lists-using-python-recursion
In [39]: [{"a":1}]+ [{"b":2}]
Out[39]: [{'a': 1}, {'b': 2}]

In [40]: [ [3, 4, 5] ] + [[9]]
Out[40]: [[3, 4, 5], [9]]

In [41]: [ [3, 4, 5] ] + [9]
Out[41]: [[3, 4, 5], 9]

In [42]: [ [3, 4, 5] ] + []
Out[42]: [[3, 4, 5]]

In [43]:
"""
class Solution:
    def validate(self, S, chosen):
        return True
    def select(self, S, chosen):
        ans = []
        print("select:choose:%s" % chosen)
        for i in chosen.strip().split():
            ans.append(S[int(i)])
        return ans
    def rec(self, S, i, chosen, sz):
        ans = {}
        #logging.debug("rec(%s, %s, %s, %s)" % (S, i, chosen, sz))
        if i == len(S):
            if len(chosen.strip().split()) == sz:
                #print(chosen)
                if self.validate(S, chosen):
                    ret = self.select(S, chosen)
                    print("ret:%s"%ret)
                    return [ret]
                else: return []
            else:
                return []
        else:
            ans = []
            for tmp in self.rec(S, i+1, chosen + " %s" % i, sz):
                ans.append(tmp)
            for tmp in self.rec(S, i+1, chosen, sz):
                ans.append(tmp)
            return ans


    def sol(self, S):
        if len(S) == 0: return None
        sz = len(S[0])
        return self.rec(S, 0, "", sz)

import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
S = ["ball", "area", "lead", "lady", "soup"]
foo = Solution()
ret = foo.sol(S)
print (ret)