"""
29. Stack from Queues
Question: Implement a LIFO stack with basic functionality (push and pop) using FIFO
queues to store the data.
Solution: https://www.byte-by-byte.com/stackfromqueues/
"""


"""
*         o    
4 <- 5 <- 9 <- 0 <- -2
pop(o)
add(4)
"""
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        curr = self.head
        stack = []
        while curr:
            stack.append( str(curr.val) )
            curr = curr.next
        return "->".join(stack)

    def add(self, x):
        node = Node(x)
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def pop(self):
        if self.head is None:
            raise IndexError
        ret = self.head

        self.head = self.head.next
        return ret

class LIFO(Queue):
    def __init__(self):
        pass

    def add(self, x):
        super().add(x)
    """
    *         o    
    4 <- 5 <- 9 <- 0 <- -2
    pop(o)
    add(4)
    """
    def pop(self):
        ret = self.tail






s = Queue()
s.add(3)
s.add(4)
s.add(-2)
print(s)
print(s.pop().val)
print(s)

