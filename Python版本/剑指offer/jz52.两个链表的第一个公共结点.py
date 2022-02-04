# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        p1, p2 = pHead1, pHead2
        p1FirstTime = p2FirstTime = True
        while True:
            if p1 == p2:
                return p1
            elif p1 == None and p1FirstTime:
                p1 = pHead2
                p1FirstTime = False
            elif p2 == None and p2FirstTime:
                p2 = pHead1
                p2FirstTime = False
            elif p1 == None or p2 == None:
                return None

            if p1 == p2:
                return p1

            if p1 != None:
                p1 = p1.next

            if p2 != None:
                p2 = p2.next








