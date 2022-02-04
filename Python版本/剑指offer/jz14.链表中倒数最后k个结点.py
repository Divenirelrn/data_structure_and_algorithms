# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead, k):
        # write code here
        if not pHead or k == 0:
            return None

        dummyNode = ListNode(None)
        dummyNode.next = pHead
        pHead = dummyNode

        fast = pHead
        slow = pHead

        j = 1
        while j < k and fast:
            fast = fast.next
            j += 1

        if j < k or not fast.next:
            return None

        while fast.next:
            fast = fast.next
            slow = slow.next

        return slow

