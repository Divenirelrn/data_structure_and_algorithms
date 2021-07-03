
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def inner(root):
            if root.left == None and root.right == None:
                return 1

            left_num = right_num = 0
            if root.left:
                left_num = inner(root.left)

            if root.right:
                right_num = inner(root.right)

            return max(1+left_num, 1+right_num)

        return inner(root)