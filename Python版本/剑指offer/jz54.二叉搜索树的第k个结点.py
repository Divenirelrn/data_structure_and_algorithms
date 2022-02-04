# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param proot TreeNode类
# @param k int整型
# @return int整型
#
class Solution:
    def KthNode(self, proot: TreeNode, k: int) -> int:
        # write code here
        if proot == None:
            return -1

        def inOrder(root):
            if root.left:
                inOrder(root.left)

            nodeList.append(root.val)

            if root.right:
                inOrder(root.right)

        nodeList = list()
        inOrder(proot)
        if k < 1 or k > len(nodeList):
            return -1
        return nodeList[k - 1]





