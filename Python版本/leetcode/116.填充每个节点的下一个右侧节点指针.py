
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root

        def inner(root):
            if not root.left and not root.right:
                return

            root.left.next = root.right

            inner(root.left)
            inner(root.right)

            p1 = root.left
            p2 = root.right
            while p1.right:
                p1 = p1.right
                p2 = p2.left
                p1.next = p2

            return root

        return inner(root)


#解法二：利用next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root

        root.left.next = root.right
        leftmost = root.left
        while leftmost.left:
            p = leftmost
            while p:
                p.left.next = p.right

                if p.next:
                    p.next.left.next = p.next.right
                    p.right.next = p.next.left

                p = p.next

            leftmost = leftmost.left

        return root