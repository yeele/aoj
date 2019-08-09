class Solution:
    def map(self, digit):
        a = {
            "2":['a', 'b', 'c'],
            "3":['d', 'e', 'f'],
            "4":['g', 'h', 'i'],
            "5":['j', 'k', 'l'],
            "6":['m', 'n', 'o'],
            "7":['p', 'q', 'r', 's'],
            "8":['t', 'u', 'v'],
            "9":['w', 'x', 'y', 'z']
        }
        assert(digit in a)
        return a[digit]

    def comb(self, choice1, choice2):
        patterns = []
        for a in choice1:
            for b in choice2:
                patterns.append(a+b)
        return patterns

    def rec(self, digits):
        if len(digits) == 1:
            return self.map(digits)
        else:
            return self.comb(self.map(digits[0]), self.rec(digits[1:]))
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits.strip() == "": return []
        return self.rec(digits)
            
        