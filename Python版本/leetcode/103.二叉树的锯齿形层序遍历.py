
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = []
        temp = []
        queue.append((root, 1))
        base = 2
        order = 1

        while len(queue):
            if order == 1:
                node, idx = queue.pop(0)

                if idx <= base - 1:
                    temp.append(node.val)
                else:
                    ans.append(temp[:])
                    queue.insert(0, (node, idx))
                    temp = []
                    base *= 2
                    order = -order
                    continue

                if node.left:
                    queue.append((node.left, 2 * idx))

                if node.right:
                    queue.append((node.right, 2 * idx + 1))
            else:
                node, idx = queue.pop()

                if idx <= base - 1:
                    temp.append(node.val)
                else:
                    ans.append(temp[:])
                    queue.append((node, idx))
                    temp = []
                    base *= 2
                    order = -order
                    continue

                if node.right:
                    queue.insert(0, (node.right, 2 * idx + 1))

                if node.left:
                    queue.insert(0, (node.left, 2 * idx))

        if len(temp):
            ans.append(temp[:])

        return ans