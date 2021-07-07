
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def inner(root):
            if root.left == None and root.right == None:
                return True, 1

            is_left = is_right = True
            left_height = right_height = 0
            if root.left:
                is_left, left_height = inner(root.left)

            if root.right:
                is_right, right_height = inner(root.right)

            ans = left_height - right_height if left_height >= right_height else right_height - left_height
            return ans <= 1 and is_left and is_right, max(left_height + 1, right_height + 1)


        return inner(root)[0]