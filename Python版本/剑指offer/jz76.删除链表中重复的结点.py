# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        # write code here
        dummyNode = ListNode(-1)
        dummyNode.next = pHead
        p1 = dummyNode
        p2 = p1.next
        while p2:
            isDuply = 0
            while p2.next and p2.val == p2.next.val:
                p2 = p2.next
                isDuply = 1

            p2 = p2.next
            if isDuply:
                p1.next = p2
            else:
                p1 = p1.next

        return dummyNode.next