#https://www.youtube.com/watch?v=Jg4E4KZstFE
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "val:%s, left:%s, right:%s" % (self.val,
                                              self.left.val if self.left else "none",
                                              self.right.val if self.right else "none",
                                              )
def bt_sum(node, k, path):
    paths = []
    if node:
        rest = k - node.val
        path_copy = path[:]
        path_copy.append(node.val)
        is_leaf = node.left is None and node.right is None
        if is_leaf:
            if rest == 0:
                return [path_copy]
            else:
                return []
        else:
            paths += bt_sum(node.left, rest, path_copy)
            paths += bt_sum(node.right, rest, path_copy)
    return paths


root = TreeNode(10)
root.left = TreeNode(16)
root.right = TreeNode(5)
root.left.right = TreeNode(-3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(11)

path = []
ans = bt_sum(root, 26, path)
print(ans)