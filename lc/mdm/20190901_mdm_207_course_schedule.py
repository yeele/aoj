#Definition for singly-linked list.

def timeit(method):
    def timed(*args, **kw):
        global calc
        calc = defaultdict(int)
        print ('===========')
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.8f ms' % (method.__name__, (te - ts) * 1000))
        print("calc %s times" % sum(calc.values()))
        return result
    return timed


from typing import List
import sys
import logging
import itertools
from collections import defaultdict
import time
#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
    def __str__(self):
        nodes = [nd.val for nd in self.neighbors]
        return "%s, %s" % (self.val, nodes)

class GraphNode(Node):
    def __init__(self, val, neighbors):
        super().__init__(val, neighbors)
        self.visitted = False
    def __init__(self, node):
        super().__init__(node.val, node.neighbors)
        self.visitted = False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        logging.debug("nc:%s, prere:%s" % (numCourses, prerequisites))
        length = len(prerequisites)
        buffer = length * 2
        visit = [False] * buffer
        needs = [[]] * buffer
        stack = []
        if length <= 0: return True
        for i, pair in enumerate(prerequisites):
            try:
                c, p = pair
            except:
                continue
            logging.debug("course:%s, preprequisite:%s" % (c, p))
            #visit[i] = True
            needs[c] = needs[c] + [p]
            stack.append(c)

        if sum([len(x) for x in needs]) == 0: return True
        if len(stack) <= 0: return False

        non_cyclic = 0
        tmp = 0
        while len(stack) > 0:
            c = stack.pop()
            if visit[c]:
                non_cyclic -= tmp
                tmp = 0
                return False
            else:
                visit[c] = True
                for pc in needs[c]:
                    stack.append(pc)
            non_cyclic += 1
            tmp += 1
        return True



samples = [
    # (2, [[1, 0]], True),
    # (2, [[1, 0], [0, 1]], False),
    # (1, [[]], True),
    # (3, [[1, 0]], False),
    (3, [[1, 0], [2, 0]], True),
]
for k, S, expected in samples:
    print("-"*20)
    print("k:%s, S:%s" % (k, S))
    ans = Solution().canFinish(k, S)
    #assert ans == expected, "(%s, %s) => %s but %s was expected" % (k, S, ans, expected)
    print("(%s, %s) = %s as expected!" % (k, S, ans))
