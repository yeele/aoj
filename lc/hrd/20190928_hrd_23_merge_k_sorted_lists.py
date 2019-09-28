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



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
普通位にやると、毎回kの比較が入るのでO(N*k)となる
だけどheapを使えばO(N*2)で済む, 
ちょっとまて正確にあｈheappush(logN)だからO(NlogN + N)
"""
# 0953am thinking
# 0953am implement start
# 0957am implenent done
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for node in lists:
            curr = node
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        head = ListNode('start')
        curr = head
        while len(heap) > 0:
            n = heapq.heappop(heap)
            curr.next = ListNode(n)
            curr = curr.next
        return head.next




class Solution_20190907:
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



