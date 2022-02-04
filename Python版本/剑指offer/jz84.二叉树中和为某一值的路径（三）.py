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
# @param sum int整型
# @return int整型
#
class Solution:
    def FindPath(self, root: TreeNode, sum: int) -> int:
        # write code here
        res = 0

        def count(root, s):
            nonlocal res
            if not root:
                return
            if s - root.val == 0:
                res += 1

            count(root.left, s - root.val)
            count(root.right, s - root.val)

        def findPath(root, s):
            if not root:
                return
            count(root, s)
            findPath(root.left, s)
            findPath(root.right, s)

        findPath(root, sum)
        return res