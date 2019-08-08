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

    def set(self, node):
        self.next = node


class Solution:
    def toNum(self, node: ListNode):
        curr = node
        stack = []
        while curr:
            x = curr.val
            stack.append(x)
            curr = curr.next

        i = 0
        num = 0
        while len(stack) > 0:
            x = stack.pop(0)
            num += (x * (10**i))
            i += 1
        return num

    """
    has overflow problem...
    9223372036854775807
    1000000000000000000000000000001
    """
    def toLinkedList_deprecated(self, num):
        n = num
        curr = None
        root = None
        if n == 0: return ListNode(0)
        while n > 0:
            print("n:%s" % n)
            x = n % 10
            if curr:
                curr.next = ListNode(x)
                curr = curr.next
            else:
                curr = ListNode(x)
                root = curr
            n = int(n / 10)
        return root

    def toLinkedList(self, num):
        n = str(num)
        curr = None
        root = None
        if n == '0': return ListNode(0)
        while len(n) > 0:
            x = int(n[-1])
            if curr:
                curr.next = ListNode(x)
                curr = curr.next
            else:
                curr = ListNode(x)
                root = curr
            n = n[:-1]
        return root

    #@timeit
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toNum(l1)
        b = self.toNum(l2)
        logging.debug("a:%s, b:%s" % (a, b))
        if a > 0 and b == 0:
            return l1
        elif b > 0 and a == 0:
            return l2
        else:
            return self.toLinkedList(a+b)



import logging
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

def printLinkedList(node: ListNode):
    stack = []
    while node:
        stack.append(str(node.val))
        node = node.next
    return "->".join(stack)

a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)

# a = ListNode(0)
# b = ListNode(0)

# a = ListNode(1)
# a.next = ListNode(8)
# b = ListNode(0)


# a = ListNode(9)
# a.next = ListNode(8)
# b = ListNode(1)


a = ListNode(1)
a.next = ListNode(0)
a.next.next = ListNode(0)
a.next.next.next = ListNode(0)
a.next.next.next.next = ListNode(0)
a.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
a.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(1)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)

logging.debug("a: %s" % printLinkedList(a))
logging.debug("b: %s" % printLinkedList(b))
ans = Solution().addTwoNumbers(a, b)
logging.info("ans: %s" % printLinkedList(ans))
import sys
print(sys.maxsize)