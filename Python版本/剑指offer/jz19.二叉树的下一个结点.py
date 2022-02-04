# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        # find root
        p = pNode
        while p.next:
            p = p.next
        pRoot = p

        def inOrder(root):
            if root.left:
                inOrder(root.left)

            nodeList.append(root)

            if root.right:
                inOrder(root.right)

        nodeList = list()
        inOrder(pRoot)

        n = len(nodeList)
        for i in range(n):
            print(nodeList[i].val)
            if nodeList[i] == pNode:
                return nodeList[i + 1] if i < n - 1 else None


#方法二：
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        # find root
        p = pNode
        while p.next:
            p = p.next
        pRoot = p

        if pNode.right != None:
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left

            return pRight

        if pNode.next != None and pNode.next.left == pNode:
            return pNode.next

        if pNode.next != None and pNode.next.right == pNode:
            pNext = pNode.next
            while pNext.next and pNext.next.right == pNext:
                pNext = pNext.next

            return pNext.next

        return None


