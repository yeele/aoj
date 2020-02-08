class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.root = None

    def last(self):
        # last node in balanced tree
        if self.root is None: return None
        layer = [self.root]
        while layer:
            next_layer = []
            leaves = []
            for node in layer:
                if node:
                    next_layer.append(node.left)
                    next_layer.append(node.right)
                    if node.left is None or node.right is None:
                        leaves.append(node)
            layer = next_layer
        return leaves[-1]

    def set_val(self, val, node):
        new_node = Node(val)
        if node.left is None:
            node.left = new_node
        elif node.right is None:
            node.right = new_node
        return new_node


    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        # find the place where i fit
        new_node = None
        stack = [self.root]
        while stack:
            next_layer = []
            for node in stack:
                if node:
                    if node.val > val:
                        node.val = val
                        last_node = self.last()
                        new_node = self.set_val(val, last_node)
                        break
                    next_layer.append(node.left)
                    next_layer.append(node.right)
        return new_node


    def bubble(self, node):
        pass

    def pop(self):
        if self.root is None:
            raise IndexError
        value = self.root.val
        # reconstruct
        # Todo.
        return value





