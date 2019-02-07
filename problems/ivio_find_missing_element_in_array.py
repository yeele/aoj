#-*- coding: utf-8 -*-

class Solution:
    def find_missing(self, list1, list2):
        """
        condition: must be exactly 1 element is missing, all others are same
        :param list1:
        :param list2:
        :return:
        """
        return sum(list1) - sum(list2)







sol: Solution = Solution()
print(sol.find_missing([1, 3, 9, 7], [3, 7, 1]))

"""
time complexity: O(N)
spce complexity: O(N)
"""