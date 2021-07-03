# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = []
        temp = []
        queue.append((root, 1))
        base = 2

        while len(queue):
            node, idx = queue.pop(0)
            if idx <= base - 1:
                temp.append(node.val)
            else:
                ans.append(temp[:])
                temp = [node.val]
                base *= 2

            if node.left:
                queue.append((node.left, 2 * idx))

            if node.right:
                queue.append((node.right, 2 * idx + 1))

        ans.append(temp[:])

        return ans
