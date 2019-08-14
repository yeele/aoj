#Definition for singly-linked list.
from typing import List

class Solution_recursive_wrong_answer:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(filter(lambda x : len(x) == n*2, self.rec(n)))
        #return self.rec(n)

    def rec(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            patterns = self.rec(n-1)
            combs = set(patterns)
            for pattern in patterns:
                combs.add("()" + pattern)
                combs.add("(" + pattern + ")")
                combs.add(pattern + "()")
            patterns2 = self.rec(n-2)
            for pattern in patterns2:
                for patternX in self.rec(2):
                    combs.add(pattern + patternX)

            return list(combs)

class Solution:
    def rec(self, chosen, o: int, c: int) -> List[str]:
        print("chosen:%s, o:%d, c:%d" % (chosen, o, c))
        if o < 0 or c < 0:
            print("no good! = self.rec(%s, %s, %s)" % (chosen, o, c))
            return []
        elif c < o:
            print("no good2 = self.rec(%s, %s, %s)" % (chosen, o, c))
            return []
        elif c == 0:
            print("Valid!!:%s" % chosen)
            return [chosen]
        else:
            combs = []
            combs += self.rec(chosen + '(', o-1, c)
            combs += self.rec(chosen + ')', o, c-1)
            return list(set(combs))

    def generateParenthesis(self, n: int) -> List[str]:
        return self.rec("", n, n)


# print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))