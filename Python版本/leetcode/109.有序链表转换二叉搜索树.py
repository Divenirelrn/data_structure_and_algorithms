
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def inner(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            left_node = inner(left, mid-1)
            right_node = inner(mid + 1, right)

            root.left = left_node
            root.right = right_node

            return root

        p = head
        nums = []
        while p != None:
            nums.append(p.val)
            p = p.next

        len_n = len(nums)
        root = inner(0, len_n - 1)

        return root