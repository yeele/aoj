#-*- coding: utf-8 -*-
from typing import List
import math

import time
def timeit(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed: %s" % elapsed)
        return ret
    return wrapped

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        head = ListNode('start')
        curr_new = head
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    curr_new.next = ListNode(curr1.val)
                    curr1 = curr1.next
                else:
                    curr_new.next = ListNode(curr2.val)
                    curr2 = curr2.next
            elif curr1:
                curr_new.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr_new.next = ListNode(curr2.val)
                curr2 = curr2.next
            curr_new = curr_new.next
        return head.next