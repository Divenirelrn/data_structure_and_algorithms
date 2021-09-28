
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        queue = list()
        queue.append(node)
        visited = dict()
        visited[node] = Node(node.val)
        while len(queue):
            n = queue.pop(0)

            for inode in n.neighbors:
                if inode not in visited:
                    queue.append(inode)
                    visited[inode] = Node(inode.val)

                visited[n].neighbors.append(visited[inode])

        return visited[node]

