#https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def validate(self, s):
        if s == "()" or s == "{}" or s == "[]": return True
        else: return False
    def pair(self, a):
        if a == "(": return ")"
        elif a == "{": return "}"
        elif a == "[": return "]"
        else: return None

    def rec(self, s):
        print("rec:%s" % s)
        if len(s) == 2:
            return self.validate(s)
        elif len(s) > 2 and len(s) % 2 == 0:
            if self.validate(s[0:2]):
                return self.rec(s[2:])
            elif self.validate(s[-2]+s[-1]):
                return self.rec(s[:-2])
            else:
                #if self.validate(s[0]+s[-1]):return self.rec(s[1:-1])
                if self.pair(s[0]) is None: return False
                i = s.find(self.pair(s[0]))
                if i >= 0:
                    if i == len(s)-1:
                        return self.rec(s[1:i])
                    else:
                        return self.rec(s[1:i]) and self.rec(s[i+1:])
                else: return False
        else:
            #"[({(())}[()])]"
            #"({(())}[()])"
            #"{(())}[()]"
            #"{(())}[()]"
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.strip() == "": return True
        return self.rec(s)