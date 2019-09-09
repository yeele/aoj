#-*- coding: utf-8 -*-
from typing import List
import logging

#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

import heapq
"""
this one caused LTE error with this case. 
https://leetcode.com/submissions/detail/258598348/
"""
class MedianFinder_lte:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # bst, then preorder to find median
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)


    def findMedian(self) -> float:
        sz = len(self.heap)
        n = (sz // 2) + 1
        tmp = heapq.nsmallest(n, self.heap)
        if sz == 1:
            return tmp[0]
        else:
            if sz % 2 == 0:
                return (tmp[-2] + tmp[-1]) / 2
            else:
                return tmp[-1]

class MedianFinder_botsu:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # bst, then preorder to find median
        self.max_heap = [] # smaller values
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        heapq.heappush(self.median_heap, num)



    def findMedian(self) -> float:
        sz = len(self.heap)
        n = (sz // 2) + 1
        tmp = heapq.nsmallest(2, self.median_heap)
        if sz == 1:
            return tmp[0]
        else:
            if sz % 2 == 0:
                return (tmp[0] + tmp[1]) / 2
            else:
                return tmp[0]


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # bst, then preorder to find median
        self.max_heap = [] # smaller values
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        heapq.heappush(self.median_heap, num)



    def findMedian(self) -> float:
        sz = len(self.heap)
        n = (sz // 2) + 1
        tmp = heapq.nsmallest(2, self.median_heap)
        if sz == 1:
            return tmp[0]
        else:
            if sz % 2 == 0:
                return (tmp[0] + tmp[1]) / 2
            else:
                return tmp[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()