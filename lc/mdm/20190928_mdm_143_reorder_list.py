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
1142am start thinking
1152am still implementing
1158am done impelemting (draft)
1205pm pause....
1245pm resume
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        1->2->3->4
        1, 4, 2, 3
        1->2->3->4->5
        1, 5, 2, 4, 3
        """
        curr = head
        sz = 0
        array = []
        while curr:
            sz += 1
            array.append(curr)
            curr = curr.next


        curr = head
        stop = sz//2 if sz % 2 == 0 else (sz//2)+1
        print("sz:%s, stop:%s" % (sz, stop))
        if sz == 1: return head
        for i in range(stop):
            print("i:%s" % i)
            left = array[i]
            right = array[sz-1-i]
            right.next = left.next
            left.next = right

        if sz % 2 == 0:
            if 0 <= stop < sz:
                array[stop].next = None
        else:
            if 0 <= stop < sz:
                array[stop-1].next = None

        return head


def print_node(node: ListNode):
    curr = node
    values = []
    while curr:
        values.append(curr.val)
        curr = curr.next
    return '->'.join(map(lambda x: str(x), values))

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

head2 = ListNode(1)
samples = [
    #head1,
    head2
]

for head in samples:
    print('-'*16)
    print('before:%s' % print_node(head))
    Solution().reorderList(head)
    print('-'*16)
    print('before:%s' % print_node(head))
