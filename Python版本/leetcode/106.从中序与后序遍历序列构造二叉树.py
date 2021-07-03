
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def inner(post_left, post_right, in_left, in_right):
            if post_left > post_right:
                return None

            post_root = postorder[post_right]
            in_root = hash_t[post_root]

            root = TreeNode(post_root)
            right_num = in_right - in_root
            right_root = inner(post_right - right_num, post_right - 1, in_root + 1, in_right)
            left_root = inner(post_left, post_right - right_num - 1, in_left, in_root - 1)

            root.right = right_root
            root.left = left_root

            return root

        n = len(inorder)
        hash_t = {val: idx for idx, val in enumerate(inorder)}

        return inner(0, n-1, 0, n-1)