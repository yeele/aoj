#-*- coding: utf-8 -*-
from typing import List
import logging

#logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
3<4>2,n<3>n,n<2>2,n<1>n,1<2>n

    4
   / \
  3   2
       \
        2
         \
          2
        /
       1
    
なんとか順番を担保しないと、同じ要素が出てきたときに、戻すパターンがでてきしまう。
なのでbfsでlevel orderで左からやる。とかのルールが必要
Q:bfsはどうか？
A: 4, 3, 2, 2, 2, 1、なるほどできそうだ。順番が担保されていてそれぞのﾉｰﾄﾞ左と右情報があればbfsでもdfsでも
いけそうだ。ただbfsのほうが直感的だろう。

擬似コードをかいてみよう。
serializeは簡単なのでdeserializeで

3<4>2,n<3>n,n<2>2,n<1>n,1<2>n

これがbfsの土台
def deserilize(node):
  stack = [node]
  while len(stack) > 0:
    another_stack= []
    while len(stack) > 0:
      another_stack.append(node.left)
      another_stack.append(node.right)
    stack.extend(another_stack)


で

def deserilize(node):
  stack = [node]
  while len(stack) > 0:
    another_stack= []
    while len(stack) > 0:
      
      another_stack.append(node.left)
      another_stack.append(node.right)
    stack.extend(another_stack)

むむ、
これはserializeやないか。むむ、むしろdfsのがやりやすいかも。


3<4>2,n<3>n,n<2>2,n<1>n,1<2>n

for ssss in  3<4>2,n<3>n,n<2>2,n<1>n,1<2>n .split(',')
  ssss = 3<4>2
  left = 3
  value = 4
  right = 2
  # instanciate
  node = Node(4) --> もしnext_parentがあれば、こいつ
  l = Node(3), r = Node(2)
  node.left = l,  node.right = r
  # ここで子供の数も数えておかないといけない。
  next_parent = node
  
とまぁ、こんな感じだ。

次はdfsでやってみる



  
3<4>2,n<3>n,n<2>2,n<1>n,1<2>n

S = 3<4>2,n<3>n,n<2>2,n<1>n,1<2>n .split(',')

def dfs(S):
    if len(S) == 1:
       clause = S.pop()
       v, l, r = S[0].split('<|>')
       Node(v)
       
すでにむずいやん。
だからやっぱbfsでいこ


bfs
info = 3<4>2,n<3>n,n<2>2,1<2>n,n<1>n
info = [4<3:2:,3<:,2<:2,2<1:,1<:] 
S = [4<3:2:,3<:,2<:2,2<1:,1<:]
i = start index 
j = end index (exclusive) like python list slice
parent_node


def bfs(S, i, j, parent):
  for child in S[i:j]: 
    l, r = child
    left, right = None(l), Node(r)
    if parent: 
      parent.left(left), parent.right(right)
    num = how many, childrene doesn, l and r has?
    if num > 0:
      for spawn in (l, r)
        bfd(S, i, j+num,spawn) 
  ssss = 3<4>2
  left = 3
  value = 4
  right = 2
  # instanciate
  node = Node(4) --> もしnext_parentがあれば、こいつ
  l = Node(3), r = Node(2)
  node.left = l,  node.right = r
  # ここで子供の数も数えておかないといけない。
  next_parent = node
  
とまぁ、こんな感じだ。

次はdfsでやってみる
      





"""
class Codec_botsu:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def str_or_empty(node: TreeNode):
            return node.val if node else ""

        if root is None: return ""
        stack = [root]
        ret = []
        while len(stack) > 0:
            another_stack= []
            while len(stack) > 0:
                node: TreeNode = stack.pop(0)
                if node is None: continue # maybe I don't need to consider. anyway.
                tmp = "%s<%s:%s" % (node.val, str_or_empty(node.left), str_or_empty(node.right))
                ret.append(tmp)
                another_stack.append(node.left)
                another_stack.append(node.right)
            stack.extend(another_stack)
        return ",".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        S = data.split(",")

        # 4, 3, 2, n, n, n, 2, n, n, n, n, n, n, 1, n
        # 4<3:2,3<:,2<:2,2<1:,1<:
        def bfs(S, i, j, node, level):
            n_children = 0
            next_i = i
            next_i = j
            for clause in S[i:j]:
                value, subs = clause.split('<')
                left_value, right_value = subs.split(':')
                #node = TreeNode(value)
                next_i += 1
                if left_value:
                    n_children += 1
                    l = TreeNode(left_value)
                    node.left = l
                if right_value:
                    n_children += 1
                    r = TreeNode(right_value)
                    node.right = r

            if node.left: bfs(S, next_i+1, j+n_children+1, l, level+1)
            if node.right: bfs(S, next_i+1, j+n_children+1, r, level+1)

        bfs(S, 0, 0, parent=None, level=1)




"""
だめだ。
全然、うまくいかない。
かれこれ計三時間は考えているぞ

このような時は
一回まっさらに戻し、ます。
新降級してから


はい。再度行きましょう。
"""






"""
まずはメモリ使い放題プランでいこうと思う
"""
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def str_or_empty(node: TreeNode):
            return node.val if node else ""

        if root == None: return ""
        values = []
        layer = [root]
        while len(layer) > 0:
            next_layer = []
            layer_elements = len(layer)
            next_point = layer_elements
            while len(layer) > 0:
                node: TreeNode = layer.pop(0)
                tmp = "%s<%s|%s:%s" % (
                    node.val,
                    str_or_empty(node.left), str_or_empty(node.right),
                    next_point
                )
                next_point -= 1
                values.append(tmp)
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
                next_point += (1 if node.left else 0) + (1 if node.right else 0)
            layer.extend(next_layer)
        return ",".join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        S = data.split(',')

        def bfs(i) -> TreeNode:
            if i >= len(S): return None
            clause = S[i].split('<')
            value = clause[0]
            tree_layer = clause[1].split(':')
            next_point = int(tree_layer[1])
            l, r = tree_layer[0].split('|')
            # number of children of this node. 0, 1 or 2
            n = len([x for x in [l, r] if x != ''])
            # 同じ階層でどれだけのノードがあるのか？
            # これを今から計算するのは大変なのでserializationの時にどうにか
            # 埋め込めないか？ A:俺の答えは逆点の発想で埋め込むことだった。
            # 同じ階層のノード数をdeserialize時に調べるにはどうしたらいいか？というように丁寧に
            # （すごいチップ！！！）文字化すると、逆点の発想を起こしやすい、逆転の発想とは、各文字の反対の意味を考えていけばいいからだ。

            # layer_elementsを単純に足すと、参照が飛んでしまった。
            # 現時点から次のlayerへの最初のindexに飛ぶにはいくつ飛べばいいのか、というような情報にしなければならない。
            # そこでlayer_elements -= 1とうのを考えた。
            # これを、serialize時に入れようと。

            # layer_elementsという考えから
            # いくつヅラせば良いかという考えへ。next_point
            logging.debug("i:%s, value:%s, l:%s, r:%s, n:%s, next_point:%s" % (i, value, l, r, n, next_point))
            node = TreeNode(value)
            if l:
                node.left = bfs(i + next_point + 0)
            if r:
                offset = 1 if l else 0
                node.right = bfs(i + next_point + offset)
            return node

        if data.strip() == "": return None
        else: return bfs(0)


# Your Codec object will be instantiated and called as such:
codec = Codec()
"""
    4
   / \
  3   2
       \
        2
       /
      1
"""
root = TreeNode(4)
l2 = TreeNode(3)
r2 = TreeNode(2)
root.left = l2
root.right = r2

r3 = TreeNode(2)
r2.right = r3
l4 = TreeNode(1)
r3.left = l4



serialized = codec.serialize(root)
logging.debug(serialized)
deserialized_node = codec.deserialize(serialized)
x = 3
y = 4

#[1,2,3,1,3,2,4]
root = TreeNode(1)
l2 = TreeNode(2)
r2 = TreeNode(3)
l3 = TreeNode(1)
r3 = TreeNode(3)
l4 = TreeNode(2)
r4 = TreeNode(4)
root.left = l2
root.right = r2
l2.left = l3
l2.right = r3
r2.left = l4
r2.right = r4

# serialized = codec.serialize(root)
# logging.debug(serialized)
# deserialized_node = codec.deserialize(serialized)
# x = 3
# y = 4

"""
ここまでして
なんとか
最初のサンプルケースで動くものができた。さて。提出してみるか。
"""


