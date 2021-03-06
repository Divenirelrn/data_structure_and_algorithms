
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def preOrder(root):
            ans.append(root.val)

            if root.left:
                preOrder(root.left)

            if root.right:
                preOrder(root.right)