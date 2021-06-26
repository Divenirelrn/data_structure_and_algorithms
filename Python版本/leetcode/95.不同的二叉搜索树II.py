
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def inner(start, end):
            if start > end:
                return [None]

            ans = []
            for i in range(start, end+1):
                left_ans = inner(start, i-1)
                right_ans = inner(i+1, end)

                for l in left_ans:
                    for r in right_ans:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        ans.append(node)

            return ans


        ans2 = inner(1, n)

        return ans2 if n else []