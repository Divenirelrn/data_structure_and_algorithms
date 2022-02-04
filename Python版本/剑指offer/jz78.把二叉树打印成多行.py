# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型二维数组
#
class Solution:
    def Print(self, pRoot: TreeNode) -> List[List[int]]:
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        res = [[pRoot.val]]
        while len(queue):
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)

            if len(temp):
                res.append(temp)

        return res