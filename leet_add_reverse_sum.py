#-*- coding: utf-8 -*-
"""
https://leetcode.com/problems/add-two-numbers/description/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def show(n):
    data = []
    curr = n
    if curr:
        data.append(curr.val)
        while curr.next:
            data.append(curr.next.val)
            curr = curr.next
    print("->".join([ str(x) for x in data]))

def toStack(n):
    stack = list()
    curr = n
    while curr:
        stack.append(curr.val)
        curr = curr.next
    return stack

def toNumber(stack: list):
    y = 0
    while len(stack) > 0:
        x = stack.pop()
        sz = len(stack)
        y += x * (10**sz)
    return y

def numberToStack(x):
    stack = list()
    for i, d in enumerate(str(x)[::-1]):
        stack.append(int(d))
    return stack



def toLinkNode(stack: list):
    cur = None
    pre = None
    while len(stack) > 0:
        x = stack.pop()
        cur = ListNode(x)
        if pre:
            cur.next = pre
        pre = cur
    return cur


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = list()
        stack2 = list()
        # show(l1)
        # show(l2)
        y = toNumber(toStack(l1)) + toNumber(toStack(l2))
        return numberToStack(y)


"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

def test():
    sol = Solution()
    #l1 = ListNode(2).next(ListNode(4).next(ListNode(3)))
    #l2 = ListNode(5).next(ListNode(6).next(ListNode(4)))

    #print(sol.addTwoNumbers(l1, l2))
    a3 = ListNode(3)
    a4 = ListNode(4)
    a4.next = a3
    a2 = ListNode(2)
    a2.next = a4


    b4 = ListNode(4)
    b6 = ListNode(6)
    b6.next = b4
    b5 = ListNode(5)
    b5.next = b6

    print(toStack(b5))
    print(toNumber([5, 6, 4]))
    nn = toLinkNode(toStack(b5))
    show(nn)
    print("===miso===")
    print(numberToStack(807))

    print(sol.addTwoNumbers(a2, b5))



mode = "test"
if mode == "test":
    test()