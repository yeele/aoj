#-*- coding: utf-8 -*-
"""
https://leetcode.com/submissions/detail/195043384/
"""

"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import re
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        #print (A, B)
        if A.find(B) != -1: return 1
        if (A+A).find(B) != -1: return 2
        found = 0
        pre = ""
        post = ""
        while True:
            try:
                idx = B.index(A)
                if found == 0: pre = B[0:idx]
                else:
                    if idx > 0:
                        return -1
                #print("B:%s" % B[idx+1:])
                #print("B:%s" % B[idx+len(A):])
                B = B[idx+len(A):]
                #print(found, B)
                found += 1
                post = B

            except Exception as e:
                #print("not found")
                break
        if found > 0 and re.match("%s.*%s" % (post, pre), A):
            #print("pre:%s, post:%s, found:%s" % (pre, post, found))
            if pre != "" and post != "": return found + 2
            elif pre != "" or post != "": return found + 1
            else: return found
        return -1

        #
        #
        # print(pattern, A, B, left)
        # if left in A+A or left == "":
        #     return self.repeatedStringMatch__slow(A, B)
        # return -1

    def repeatedStringMatch__slow(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        print("a    ")
        As = A
        for i in range(10000):
            #print(i, As)
            if B in As:
                return i+1
            As += A
            #if i == 10: break
        return -1


solver = Solution()
a = "abc"
b = "cabcabca"
a = "abcd"
b = "cdabcdab"
a = "abcabcabcabc"
b = "abac"
# time exceeded
a = "abc"
b = "aabcbabcc"
#
a = "abcd"
b = "cdabcdab"
# 22
a = "abcd"
b = "cdabcdab"

a = "abc"
b = "cabcabca"

a = "baaaabbbba"
b = "bbaaaabbbbaabaaaabbbbaabaaaabbbbaabaaaabbbbaabaaaabbbbabbaaaabbbbabbaaaabbbbabbaaaabbbbabbaaaabbbbaa"

a = "aa"
b = "a"

a = "abc"
b = "cabcabca"

a = "aaaaaaaaaaaaaaaaaaaaaab"
b = "ba"

a = "abcd"
b = "abcdb"

a = "abcd"
b = "cdabcdab"

a = "abcd"
b = "cdabcdacdabcda"

a = "a"
b = "aaaaaaaaaaaaa"
ret = solver.repeatedStringMatch(a, b)
print(ret)
