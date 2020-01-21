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

import sys
sys.setrecursionlimit(314159265)

class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        #[[7,null],[13,0],[11,4],[10,2],[1,0]]
        #[1, 10, 11, 13, 7] # pushleft
        import collections
        q = collections.deque()
        if head is None: return None
        # popleft & pushright
        q.append(head)
        cloned = {}
        while q:
            curr = q.popleft()
            cloned[curr] = Node(curr.val)
            if curr.next is not None: q.append(curr.next)
        # cloned = {1: 1', 10: 10', ..., 7:7'}
        q.append(head)
        while q:
            curr = q.popleft()
            if curr.next is not None:
                cloned[curr].next = cloned[curr.next]
                q.append(curr.next)
        # lastly, rando
        #[1', 10', 11', 13', 7']
        q.append(head)
        while q:
            curr = q.popleft()
            if curr.random is not None:
                cloned[curr].random = cloned[curr.random]
            if curr.next is not None:
                q.append(curr.next)
        return cloned[head]




# [[7,null],[13,0],[11,4],[10,2],[1,0]]
n4 = Node(1, None)
n3 = Node(10, n4)
n2 = Node(11, n3)
n1 = Node(13, n2)
n0 = Node(7, n1)
n4.random = n0
n3.random = n2
n2.random = n4
n1.random = n0
n0.random = None

ans = Solution().copyRandomList(n0)
print(ans)