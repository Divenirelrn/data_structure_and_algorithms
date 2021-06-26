# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        ans = []

        def in_traversal(root):
            if not root:
                return []

            if root.left:
                in_traversal(root.left)

            ans.append(root.val)

            if root.right:
                in_traversal(root.right)

        in_traversal(root)

        return ans
