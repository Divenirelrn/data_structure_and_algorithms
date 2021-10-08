
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = list()
        ans = dict()
        stack.append((root, 1))
        maxDepth = 0

        while len(stack):
            node, depth = stack.pop()

            ans.setdefault(depth, node.val)
            if node.left:
                stack.append((node.left, depth + 1))

            if node.right:
                stack.append((node.right, depth + 1))

            maxDepth = depth if depth > maxDepth else maxDepth

        return [ans[key] for key in range(1, maxDepth + 1)]