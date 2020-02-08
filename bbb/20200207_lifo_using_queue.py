#https://www.byte-by-byte.com/priorityqueue/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions
#一回自分で書いてみて難しかったので、回答をみた
"""
[0, 1, 2, 3, 4, 5, 6, 8, 9]

       0
      /  \
     1    2
    / \   / \
   3  4   5  6
  / \
 7   8
"""
from queue import Queue, LifoQueue
class LQueue:
    def __init__(self, max_size):
        self.q = Queue(max_size)
        self.q2 = LifoQueue()

    def push(self, x):
        self.q.put(x)

    def pop(self):
        """
        *
        3 -> 9 -> -2 -> 4 -> 1

        """
        self.q.get()





