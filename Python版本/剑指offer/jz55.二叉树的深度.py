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
# @return int整型
#
class Solution:
    def TreeDepth(self, pRoot: TreeNode) -> int:
        # write code here
        if pRoot == None:
            return 0

        def treeDepth(root):
            if not root:
                return 0

            return max(treeDepth(root.left), treeDepth(root.right)) + 1

        return treeDepth(pRoot)