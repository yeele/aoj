class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


"""
単純な問題ですが、以外と難しい。
node.xの範囲はlower, upper内であれば成立とみなすこと。
lowerとupperの敷地はfloat('-+inf')で始めると
最初のrootは常に成立。
例えば次の左ノードnode.leftもnode.xより小さくて、　〜よりも大きいというのは、
今は制限なくて、とにかく、今のおれよりも小さければよいという
やんちゃな側面だけ見てれば拾はいいんです。
バイナリーノードの関係はあくまでシンプルで！
左は俺より小さいこと！
右は俺より大きいこと！
それだけ！
そうなんけど、この処理は一緒くたにできるのはlower,upperをinfつかい回しているから。

"""
class Solution:
    """
    https://www.techseries.dev/products/algopro/categories/1831147/posts/6231427
    """
    def isValidBST(self, node):

        def is_valid(node, lower, upper):
            if node is None: return True
            if node.x <= lower or node.x >= upper:
                return False
            if not is_valid(node.left, lower, node.x):
                return False
            if not is_valid(node.right, node.x, upper):
                return False
            return True

        return is_valid(node, float('-inf'), float('inf'))


node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
print(Solution().isValidBST(node))