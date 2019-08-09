# Definition for a binary tree node.
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

class BSTIterator:

    def dfs_pre_order(self, node):
        print("dfs_pre_order:%s" % node)
        # visit
        ans = []
        if node:
            print("miso1:%s" % node)
            ans.extend(self.dfs_pre_order(node.left))
            ans.append(node.val)
            ans.extend(self.dfs_pre_order(node.right))
            return ans
        else:
            return ans


    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.ans = self.dfs_pre_order(root)
        print(self.ans)


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.ans.pop(0)




    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if len(self.ans) > 0 else False




# Your BSTIterator object will be instantiated and called as such:
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)
obj = BSTIterator(root)
param_1 = obj.next()
print(obj.ans)
param_2 = obj.hasNext()