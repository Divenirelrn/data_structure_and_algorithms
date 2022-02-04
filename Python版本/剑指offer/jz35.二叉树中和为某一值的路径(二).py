# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def FindPath(self, root: TreeNode, target: int) -> List[List[int]]:
        # write code here
        if not root:
            return list()

        def inner(root, total):
            if not root.left and not root.right and total + root.val == target:
                res.append(temp[:])
                return

            if not root.left and not root.right:
                return

            total += root.val
            if root.left:
                temp.append(root.left.val)
                inner(root.left, total)
                temp.pop()

            if root.right:
                temp.append(root.right.val)
                inner(root.right, total)
                temp.pop()

        res = list()
        temp = [root.val]
        inner(root, 0)

        return res