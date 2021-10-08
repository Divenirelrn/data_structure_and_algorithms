
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.cache = list()
        self.inOrder(root)
        self.idx = 0
        self.capacity = len(self.cache)


    def next(self) -> int:
        val = self.cache[self.idx]
        self.idx += 1
        return val


    def hasNext(self) -> bool:
        if self.idx < self.capacity:
            return True
        else:
            return False


    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)

        self.cache.append(root.val)

        if root.right:
            self.inOrder(root.right)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()