
class DLinkNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DLinkNode(None, None)
        self.tail = DLinkNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if self.cache.get(key, -1) == -1:
            return -1
        else:
            node = self.cache[key]
            #move to head
            self.move_to_head(node)

            #update cache
            self.cache[key] = node

            return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, -1)
        if node == -1:
            #head insert
            node = DLinkNode(key, value)
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

            #add to cache
            self.cache[key] = node
            self.size += 1

            #if size > capacity
            if self.size > self.capacity:
                #tail delete
                node = self.tail.prev
                node.prev.next = self.tail
                self.tail.prev = node.prev

                #sub cache
                del self.cache[node.key]
                self.size -= 1
        else:
            node.value = value

            #move to head
            self.move_to_head(node)

            #update cache
            self.cache[key] = node

    def move_to_head(self, node):
        #delete node
        node.prev.next = node.next
        node.next.prev = node.prev

        #insert node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)