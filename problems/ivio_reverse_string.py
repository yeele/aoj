#-*- coding: utf-8 -*-

class Solution:
    def reverse_string(self, str):
        str = list(str)
        pr = len(str) - 1
        pl = 0
        while pr > pl:
            tmp = str[pr]
            str[pr] = str[pl]
            str[pl] = tmp
            pr-=1
            pl+=1
        return str






sol: Solution = Solution()
print(sol.reverse_string("miso"))
print(sol.reverse_string("pasta"))

"""
time complexity: O(N)
spce complexity: O(N)
"""