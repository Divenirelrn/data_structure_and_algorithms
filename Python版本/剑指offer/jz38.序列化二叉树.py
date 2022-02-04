# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        def preOrder(root):
            nonlocal res
            if not root:
                res += "#,"
                return

            res += str(root.val) + ","

            preOrder(root.left)
            preOrder(root.right)

        res = ""
        preOrder(root)

        return res[:-1]

    def Deserialize(self, s):
        # write code here
        def preOrder():
            nonlocal list_s
            if not len(list_s):
                return

            val = list_s.pop(0)
            root = None
            if val != '#':
                root = TreeNode(int(val))
                root.left = preOrder()
                root.right = preOrder()

            return root

        list_s = s.split(",")
        return preOrder()


