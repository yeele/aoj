#https://note.nkmk.me/python-union-find/

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def traverse(node):
    if node is None: return
    stack = []
    curr = node
    while curr is not None or len(stack) > 0:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.right

root = Node(5)
n1 = Node(3)
n2 = Node(7)
n1.right = Node(4)
n2.left = Node(11)
root.left = n1
root.right = n2

traverse(root)