# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        # write code here
        def getAncestor(root, p, q):
            if None == root:
                return None
            if root.val == p or root.val == q:
                return root

            left = getAncestor(root.left, p, q)
            right = getAncestor(root.right, p, q)
            if not right:
                return left
            elif not left:
                return right
            else:
                return root

        return getAncestor(root, p, q).val

#方法二：利用二叉搜索树的性质
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        # write code here
        def getAncestor(root, p, q):
            if None == root:
                return None
            if root.val == p or root.val == q:
                return root

            if p < root.val and q < root.val:
                return getAncestor(root.left, p, q)
            elif p > root.val and q > root.val:
                return getAncestor(root.right, p, q)
            else:
                return root

        return getAncestor(root, p, q).val









