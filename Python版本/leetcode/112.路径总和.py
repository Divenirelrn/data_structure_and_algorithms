
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def inner(root, sum):
            sum += root.val

            if root.left == None and root.right == None and sum == targetSum:
                return True

            is_left = is_right = False
            if root.left:
                is_left = inner(root.left, sum)

            if root.right:
                is_right = inner(root.right, sum)

            return is_left or is_right

        return inner(root, 0)