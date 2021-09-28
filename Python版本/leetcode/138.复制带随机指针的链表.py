
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        begin = Node(head.val)
        hash_t = {}
        hash_t[head] = begin
        p = head

        while p:
            if p.next == None:
                hash_t[p].next = None
            else:
                if p.next not in hash_t:
                    hash_t[p.next] = Node(p.next.val)

                hash_t[p].next = hash_t[p.next]

            if p.random == None:
                hash_t[p].random = None
            else:
                if p.random not in hash_t:
                    hash_t[p.random] = Node(p.random.val)

                hash_t[p].random = hash_t[p.random]

            p = p.next

        return hash_t[head]