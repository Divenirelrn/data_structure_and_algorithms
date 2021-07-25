# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(left_root):
            nonlocal p
            node = TreeNode(left_root.val)
            p.right = node
            p = p.right

            if left_root.left:
                preorder(left_root.left)

            if left_root.right:
                preorder(left_root.right)

        if not root:
            return None

        if not root.left and not root.right:
            return root

        if not root.left:
            root.left = root.right
        else:
            p = root.left
            while p.right:
                p = p.right

            p.right = root.right

        root.right = None

        p = root
        preorder(root.left)
        root.left = None


