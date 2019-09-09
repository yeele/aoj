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

class Heap:
    def __init__(self):
        self.root = None
        self.n = 0 # number of elements


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq
class MedianFinder_why_this_doesnt_passed_wakaran:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] # smaller values
        self.min_heap = [] # larger  values


    def addNum(self, num: int) -> None:
        n = len(self.max_heap) + len(self.min_heap)
        if n == 0:
            heapq.heappush(self.max_heap, (-num, num))
        else:
            max_heap_top = self.max_heap[0][1] if len(self.max_heap) > 0 else 0
            min_heap_top = self.min_heap[0] if len(self.min_heap) > 0 else 0
            if num <= min_heap_top:
                heapq.heappush(self.max_heap, (-num, num))
            elif num > max_heap_top:
                heapq.heappush(self.min_heap, num)
            # adjust
            if len(self.max_heap) - len(self.min_heap) == 2:
                x = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, x[1])
            elif len(self.min_heap) - len(self.max_heap) == 2:
                x = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, (-x, x))



    def findMedian(self) -> float:
        if len(self.max_heap) + len(self.min_heap) == 0: return 0.0

        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0][1]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            max_heap_top = self.max_heap[0][1]
            min_heap_top = self.min_heap[0]
            avg = (max_heap_top + min_heap_top) / 2
            return avg


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] # smaller values
        self.min_heap = [] # larger  values


    def addNum(self, num: int) -> None:
        n = len(self.max_heap) + len(self.min_heap)
        if n == 0:
            heapq.heappush(self.max_heap, (-num, num))
        else:
            if num > self.max_heap[0][1]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, (-num, num))

            # adjust
            if len(self.max_heap) - len(self.min_heap) == 2:
                x = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, x[1])
            elif len(self.min_heap) - len(self.max_heap) == 2:
                x = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, (-x, x))



    def findMedian(self) -> float:
        if len(self.max_heap) + len(self.min_heap) == 0: return 0.0

        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0][1]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            max_heap_top = self.max_heap[0][1]
            min_heap_top = self.min_heap[0]
            avg = (max_heap_top + min_heap_top) / 2
            return avg


mf = MedianFinder()
mf.addNum(4)
def mf_print():
    print("max_heap:%s" % mf.max_heap)
    print("min_heap:%s" % mf.min_heap)

mf_print()
mf.addNum(7)
mf_print()