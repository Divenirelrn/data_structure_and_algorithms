
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        def inner(root, sum):
            if root.left == None and root.right == None and sum == targetSum:
                ans.append(temp[:])
                return

            if root.left:
                sum += root.left.val
                temp.append(root.left.val)
                inner(root.left, sum)
                sum -= root.left.val
                temp.pop()


            if root.right:
                sum += root.right.val
                temp.append(root.right.val)
                inner(root.right, sum)
                sum -= root.right.val
                temp.pop()

        ans = []
        temp = [root.val]
        inner(root, root.val)

        return ans