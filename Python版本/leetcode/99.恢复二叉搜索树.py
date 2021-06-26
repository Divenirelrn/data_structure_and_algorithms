
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inOrder(root):
            if root.left:
                inOrder(root.left)

            nodes.append(root)

            if root.right:
                inOrder(root.right)

        nodes = []
        inOrder(root)

        p1 = None
        p2 = None
        fir = True
        for i in range(1, len(nodes)):
            if nodes[i].val <= nodes[i-1].val:
                if fir:
                    p1 = nodes[i-1]
                    fir = False
                p2 = nodes[i]

        p1.val, p2.val = p2.val, p1.val