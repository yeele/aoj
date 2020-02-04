#https://note.nkmk.me/python-union-find/

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def rec_post(node):
    if node:
        rec_post(node.left)
        rec_post(node.right)
        node.val # visit

def postorder_traverse(node):
    if node is None: return
    stack = []
    curr = node # currはヤンキーです
    while curr is not None or len(stack) > 0:
        if curr: # ほぉ、道があるじゃねぇか。
            stack.append((curr, 1)) # 左に行ってやら！でも、その前に道に迷いたくないからツバを吐く
            curr = curr.left # そして左へ
        else:
            curr, i = stack.pop() # それ以上道がなかったので、戻ってきたら、ツバが何個かかぞえよう。
            if i == 2: # ２個ツバある！ってことは２つの帰路もう、試したべ！
                print(curr.val) # visit　だったら「ここで一言」俺の配下は調べたぜ。キラっ
                curr = None # で、も一個上に、戻るから道は探索すみってことでnone
            else: # ツバが一個しかない、
                stack.append((curr, i+1)) #左のsubtreeから帰ってきただけじゃん。だったら右行くぞ！その前にぺっ！
                curr = curr.right # 右に進む！

"""
   5
  /  \
 3     7  
  \   /
  4  11
"""
# 4, 3, 11, 7, 5

root = Node(5)
n1 = Node(3)
n2 = Node(7)
n1.right = Node(4)
n2.left = Node(11)
root.left = n1
root.right = n2

postorder_traverse(root)