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
class PriorityQueue:
    def __init__(self, max_size):
        self.heap = [0] * max_size
        self.size = 0

    def push(self, x):
        if self.size == len(self.heap):
            raise IndexError

        i = self.size
        self.heap[i] = x
        """
        [0, 1, 2, 3, 4, 5, 6, 8, 9]
        0 -> 1, 2
        1 -> 3, 4
        2 -> 5, 6
        n -> (n*2)+1, n*2+2        
        """
        while i >= 0 :
            # whose my parent!?
            par = (i + 1) // 2 - 1
            if self.heap[par] > self.heap[i]:
                break
            self.heap[par], self.heap[i] = self.heap[i], self.heap[par]
            i = par
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError
        ans = self.heap[0]
        # reconstruct
        j = self.size - 1
        self.heap[0] = self.heap[j]
        # clear
        self.heap[j]
        #bubble down
        i = 0
        while i < self.size:
            l = i * 2 + 1
            r = i * 2 + 2
            if r < self.size and self.heap[r] > self.heap[i]:
                self.heap[r], self.heap[i] = self.heap[i], self.heap[r]
                i = r
            elif self.heap[l] > self.heap[i]:
                self.heap[l], self.heap[i] = self.heap[i], self.heap[l]
                i = l
            else:
                break
        self.size -= 1
        return ans








