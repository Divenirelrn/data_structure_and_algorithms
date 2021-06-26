
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inOrder(root):
            if root.left:
                inOrder(root.left)

            nodes.append(root.val)

            if root.right:
                inOrder(root.right)

        nodes = []
        inOrder(root)

        ans = True
        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i-1]:
                ans = False
                break

        return ans
