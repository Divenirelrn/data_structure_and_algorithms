# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def doesTree1HasTree2(root1, root2):
            if not root2:
                return True

            if not root1:
                return False

            if root1.val != root2.val:
                return False

            return doesTree1HasTree2(root1.left, root2.left) and doesTree1HasTree2(root1.right, root2.right)

        def hasSubtree(root1, root2):
            if not root1 or not root2:
                return False

            return doesTree1HasTree2(root1, root2) or hasSubtree(root1.left, root2) or hasSubtree(root1.right, root2)

        return hasSubtree(pRoot1, pRoot2)

