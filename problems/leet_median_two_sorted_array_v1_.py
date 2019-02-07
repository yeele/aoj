#-*- coding: utf-8 -*-
"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = 0
        ttl_sz = len(nums1) + len(nums2)
        tmp = int(ttl_sz/2)
        if (ttl_sz) % 2 == 0:
            indice = [tmp, tmp-1]
            indice_num = 2
        else:
            indice = [tmp]
            indice_num = 1

        for idx in indice:
            assert(idx < ttl_sz - 1)
        c = 0
        ttl = 0
        cur = 0
        while indice:
            #logging.debug("indice:%s, i:%s, j:%s, c:%s, ttl:%s, cur:%s" % (indice, i, j, c, ttl, cur))
            if i >= len(nums1):
                cur = nums2[j]
                j+=1
            elif j >= len(nums2):
                cur = nums1[i]
                i+=1
            elif nums1[i] < nums2[j]:
                cur = nums1[i]
                i+=1
            elif nums1[i] >= nums2[j]:
                cur = nums2[j]
                j+=1

            if c in indice:
                ttl += cur
                indice.pop()
            c+=1
        return ttl/indice_num



import logging
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.basicConfig(level=logging.INFO, format="%(message)s")
nums1 = [1, 3]
nums2 = [2]
nums1 = [1, 2]
nums2 = [3, 4]
nums1 = [1, 3, 9]
nums2 = [2, 9]
foo = Solution()
print (foo.findMedianSortedArrays(nums1, nums2))
