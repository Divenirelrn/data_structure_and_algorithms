# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2

        dummyNode = ListNode(None)
        pHead = dummyNode
        p = pHead

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next

            p = p.next

        while p1:
            p.next = p1
            p1 = p1.next
            p = p.next

        while p2:
            p.next = p2
            p2 = p2.next
            p = p.next

        return pHead.next
