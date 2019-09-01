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


from collections import defaultdict
class Solution:


    def cloneGraph(self, node: List[Node]) -> List[Node]:
        stack = []
        visitted = defaultdict(bool)
        cloned = {}
        if node == None: return None
        stack.append(node)
        def get_newobj(node: Node) -> Node:
            if node is None: return None
            ref = id(node)
            if ref not in cloned.keys():
                newobj = Node(node.val, [])
                cloned[ref] = newobj
            return cloned[ref]
        def add_neighbor(node:Node, neighbor:Node):
            if node is None: return
            if neighbor is None: return
            if neighbor not in node.neighbors:
                node.neighbors.append(neighbor)

        while len(stack):
            curr = stack.pop(0)
            ref = id(curr)
            newobj = get_newobj(curr)
            if not visitted[ref]:
                visitted[id(curr)] = True
                logging.debug("curr.val is %s" % curr.val)
                for nextnode in curr.neighbors:
                    stack.append(nextnode)
                    add_neighbor(newobj, get_newobj(nextnode))
                    logging.debug("cur.neighbor's node, which is nextnode val is %s" % nextnode.val)
        return cloned[id(node)]


    def dfs(self, node: List[Node]) -> List[Node]:
        stack = []
        visitted = defaultdict(bool)
        if node == None: return None
        stack.append(node)
        while len(stack):
            curr = stack.pop(0)
            ref = id(curr)
            if not visitted[ref]:
                visitted[id(curr)] = True
                logging.debug("curr.val is %s" % curr.val)
                for nextnode in curr.neighbors:
                    stack.append(nextnode)


n1 = Node(1, [])
n2 = Node(2, [])
n3 = Node(3, [])
n4 = Node(4, [])
n1.neighbors.append(n2)
n1.neighbors.append(n4)
n2.neighbors.append(n3)
n2.neighbors.append(n1)
n3.neighbors.append(n4)
n3.neighbors.append(n2)
n4.neighbors.append(n1)
n4.neighbors.append(n3)


ans = Solution().cloneGraph(n1)
#assert ans == expected, "(%s) => %s but %s was expected" % (node ans, expected)
print("(%s) = %s as expected!" % (n1, ans))

