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
        if not root or not root.left and not root.right:
            return root

        if root.left and root.right:
            root.left.next = root.right

        if root.left:
            leftmost = root.left
        elif root.right:
            leftmost = root.right

        while leftmost:
            p1 = leftmost
            p2 = leftmost.next
            while p1:
                if p1.left and p1.right:
                    p1.left.next = p1.right

                if not p2:
                    break

                if p2.left and p2.right:
                    p2.left.next = p2.right

                if not p1.left and not p1.right:
                    p1 = p2
                    p2 = p2.next
                elif not p2.left and not p2.right:
                    p2 = p2.next
                else:
                    if p1.right:
                        if p2.left:
                            p1.right.next = p2.left
                        else:
                            p1.right.next = p2.right
                    else:
                        if p2.left:
                            p1.left.next = p2.left
                        else:
                            p1.left.next = p2.right

                    p1 = p2
                    p2 = p2.next

            p = leftmost
            leftmost = None
            while p:
                if p.left:
                    leftmost = p.left
                    break
                if p.right:
                    leftmost = p.right
                    break

                p = p.next

        return root