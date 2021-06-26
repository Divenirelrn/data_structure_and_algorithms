
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if p and not q or q and not p:
            return False

        def inner(root1, root2):
            isLeft = isRight = False
            if root1.left and root2.left:
                isLeft = inner(root1.left, root2.left)
            elif not root1.left and not root2.left:
                isLeft = True

            if root1.right and root2.right:
                isRight = inner(root1.right, root2.right)
            elif not root1.right and not root2.right:
                isRight = True

            return root1.val == root2.val and isLeft and isRight

        return inner(p, q)



