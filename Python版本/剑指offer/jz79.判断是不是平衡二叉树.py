# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return bool布尔型
#
class Solution:
    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:
        # write code here
        def height(root):
            if not root:
                return 0

            return max(height(root.left), height(root.right)) + 1

        def isBalanced(root):
            if not root:
                return True
            return abs(height(root.left) - height(root.right)) <= 1 \
                   and isBalanced(root.left) and isBalanced(root.right)

        return isBalanced(pRoot)