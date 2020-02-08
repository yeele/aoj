#https://note.nkmk.me/python-union-find/

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traverse(node):
    if node is None: return
    stack = []
    curr = node # currはヤンキーです
    while curr is not None or len(stack) > 0:
        # 3, 4, 4, 5, 11, 7, 7
        # []
        if curr: # ヤンキーは帰路にいます
            stack.append(curr)   # 左の道に行くんだけど、帰ってくる時の目印としてツバを吐く
            curr = curr.left   # 左にすすんだらぁ！
        else: # どうやら、行き止まりでしたね。
            curr = stack.pop() # 一個前、そうそう、ツバをつけたところに戻るぜ。
            print(curr.val)   # ここで、一言！
            curr = curr.right # 左はさっき行ったから、右いくからな！

"""
   5
  /  \
 3     7  
  \   /
  4  11
"""
# 3, 4, 5, 11, 7

root = Node(5)
n1 = Node(3)
n2 = Node(7)
n1.right = Node(4)
n2.left = Node(11)
root.left = n1
root.right = n2

traverse(root)