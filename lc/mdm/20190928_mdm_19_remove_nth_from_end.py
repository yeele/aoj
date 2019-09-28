#-*- coding: utf-8 -*-
from typing import List
import logging

#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
"""
# 1008am thinking
# 1014am implementatoin done
# 1116am 途中別のことをしたのでタイムロス、しかし場合分けが多い問題は実装が疲れるな。
# なんとかならんかねぇ。
# one passでもできるらしいだけど、それは、配列にnode記憶していって、やる。かな。
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1
        sz = i
        target = sz - (n)
        print(sz, target)
        if target == 0 and sz == 1: return None
        i = 0
        if target == 0 and sz >= 2:
            head = head.next
            return head
        curr = head
        while curr:
            if i == target-1:
                curr.next = curr.next.next if curr.next else None
                curr = curr.next
            else:
                curr = curr.next
            i += 1
        return head


