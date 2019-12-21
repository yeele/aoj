INT_MIN = -2**31
INT_MAX = 2**31

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def rec(post, root_idx, root_val, min, max):
    # Base case
    if (root_idx < 0):
        return None

    root = None
    if (root_val > min and root_val < max) :
        root = newNode(root_val)
        root_idx -= 1
        next_root_val = post[root_idx]

        if (root_idx >= 0) :
            root.right = rec(post, root_idx, next_root_val, root_val, max)
            root.left  = rec(post, root_idx, next_root_val, min,      root_val)

    return root

def constructTree (post, size) :
    root_idx = size-1
    root_val = post[size-1]
    return rec(post, root_idx, root_val, INT_MIN, INT_MAX)

# A utility function to prinorder
# traversal of a Binary Tree
def printInorder (node) :

    if (node == None) :
        return
    printInorder(node.left)
    print(node.data, end = " ")
    printInorder(node.right)

# Driver Code
if __name__ == '__main__':
    post = [1, 7, 5, 50, 40, 10]
    size = len(post)

    root = constructTree(post, size)

    print("Inorder traversal of the",
          "constructed tree: ")
    printInorder(root)

# This code is contributed
# by SHUBHAMSINGH10
