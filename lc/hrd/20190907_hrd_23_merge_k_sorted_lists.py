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
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        #heapq.heapify(heap)
        for listnode in lists:
            curr = listnode
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        if len(heap) == 0: return None
        val = heapq.heappop(heap)
        root = ListNode(val)
        curr = root
        while len(heap) > 0:
            val = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
        return root



