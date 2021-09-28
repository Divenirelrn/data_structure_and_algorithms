
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def inner(root):
            nonlocal total, temp
            if not root.left and not root.right:
                total += int(temp)
                return

            if root.left:
                temp += str(root.left.val)
                inner(root.left)
                temp = temp[:-1]

            if root.right:
                temp += str(root.right.val)
                inner(root.right)
                temp = temp[:-1]

        total = 0
        temp = str(root.val)
        inner(root)

        return total