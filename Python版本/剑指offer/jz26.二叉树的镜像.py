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
# @return TreeNode类
#
class Solution:
    def Mirror(self, pRoot: TreeNode) -> TreeNode:
        # write code here
        if not pRoot:
            return None

        def buildTree(root1, root2):
            if not root1.left and not root1.right:
                return

            if root1.left:
                root2.right = TreeNode(root1.left.val)
                buildTree(root1.left, root2.right)

            if root1.right:
                root2.left = TreeNode(root1.right.val)
                buildTree(root1.right, root2.left)

        resRoot = TreeNode(pRoot.val)
        buildTree(pRoot, resRoot)

        return resRoot

#方法二：
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
# @return TreeNode类
#
class Solution:
    def Mirror(self, pRoot: TreeNode) -> TreeNode:
        # write code here
        if not pRoot:
            return None

        pRoot.left, pRoot.right = pRoot.right, pRoot.left

        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)

        return pRoot
