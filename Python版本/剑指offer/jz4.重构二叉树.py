# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self, pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        n = len(pre)
        if n == 0:
            return None

        def buildTree(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None

            preRoot = preLeft
            inRoot = inMap[pre[preRoot]]
            root = TreeNode(pre[preRoot])
            subLeftSize = inRoot - inLeft
            root.left = buildTree(preLeft + 1, preLeft + subLeftSize, inLeft, inRoot - 1)
            root.right = buildTree(preRoot + subLeftSize + 1, preRight, inRoot + 1, inRight)

            return root

        inMap = {vin[i]: i for i in range(n)}
        return buildTree(0, n - 1, 0, n - 1)