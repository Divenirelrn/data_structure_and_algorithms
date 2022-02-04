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
# @return bool布尔型
#
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # write code here
        if not root:
            return False

        def hasPath(root, s):
            if not root:
                return False
            if not root.left and not root.right and s - root.val == 0:
                return True

            return hasPath(root.left, s - root.val) or hasPath(root.right, s - root.val)

        return hasPath(root, sum)