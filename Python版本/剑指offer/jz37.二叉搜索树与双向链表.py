# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        def inOrder(root):
            nonlocal preNode
            if root.left:
                inOrder(root.left)

            root.left = preNode
            if preNode:
                preNode.right = root
            preNode = root

            if root.right:
                inOrder(root.right)

        if not pRootOfTree:
            return None

        p = pRootOfTree
        while p.left:
            p = p.left

        preNode = None
        inOrder(pRootOfTree)

        return p


