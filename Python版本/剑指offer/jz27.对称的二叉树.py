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
    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        # write code here
        def isSame(pRoot1, pRoot2):
            if not pRoot1 and not pRoot2:
                return True

            if not pRoot1 or not pRoot2:
                return False

            return pRoot1.val == pRoot2.val and isSame(pRoot1.left, pRoot2.right) \
                   and isSame(pRoot1.right, pRoot2.left)

        return isSame(pRoot, pRoot)
