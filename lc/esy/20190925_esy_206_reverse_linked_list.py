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
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            tsugi = cur.next
            cur.next = pre
            pre = cur
            cur = tsugi
        return pre


def p(node: ListNode):
    cur = node
    while cur:
        print(cur.val, end="->")
        cur = cur.next
    print(cur)


a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c
d = ListNode(4)
c.next = d
e = ListNode(5)
d.next = e
p(a)
ans = Solution().reverseList(a)
p(ans)