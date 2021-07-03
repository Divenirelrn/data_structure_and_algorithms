# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or not root.left and not root.right:
            return True

        def inner(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False

            isSymOuter = inner(p.left, q.right)
            isSymInner = inner(p.right, q.left)

            return p.val == q.val and isSymInner and isSymOuter

        return inner(root.left, root.right)