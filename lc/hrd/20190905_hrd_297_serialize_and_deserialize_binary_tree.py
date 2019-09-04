≥#-*- coding: utf-8 -*-
from typing import List
import logging

logging.basicConfig(level=logging.WARN, format="%(message)s")
#logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.basicConfig(level=logging.DEBUG, format="%(message)s")

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
  
  next_parent = node
  
  
  
  
  
  


"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



samples = [
    #([100, 4, 200, 1, 3, 2], 4),
    ([100,4,200,1,3,2], 4),
    # ([1, 2, 3, 10, 4, 9, 5], 5),
    # ([9, 5, 8, 1, 4, 10, 13, 7, 11, 12, 3, 2], 7),
]
for S, expected in samples:
    print("-"*20)
    ans = Solution().longestConsecutive(S)
    #assert ans == expected, "(%s) => %s but %s was expected" % (S, ans, expected)
    print("(%s) = %s as expected!" % (S, ans))

