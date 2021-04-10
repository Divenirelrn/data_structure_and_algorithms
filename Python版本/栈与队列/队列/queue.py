
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Queue:
    def __init__(self):
        node = Node(None)
        self.front = node
        self.rear = node

    def printQueue(self):
        temp = []
        if self.front == self.rear:
            print(temp)
            return

        p = self.front.next
        while(p != self.rear):
            temp.append(p.data)
            p = p.next

        temp.append(p.data)
        print(temp)


    def insertQueue(self, val):
        node = Node(val)

        self.rear.next = node
        self.rear = node

    def deleteQueue(self):
        if self.front == self.rear:
            return -1

        temp = self.front.next.data

        self.front.next = self.front.next.next

        if not self.front.next:
            self.rear = self.front

        return temp

    def destroyQueue(self):
        if self.front == self.rear:
            del self.front

        elif self.front.next == self.rear:
            del self.rear
            del self.front

        else:
            p = self.front.next.next
            while(p != self.rear):
                del self.front.next
                self.front = p
                p = p.next

            del self.rear
            del self.front

        return 0

if __name__ == "__main__":
    q = Queue()
    q.insertQueue(10)
    q.insertQueue(20)
    q.insertQueue(30)
    q.insertQueue(40)
    q.insertQueue(50)
    q.printQueue()

    # q.deleteQueue()
    # q.deleteQueue()
    # q.deleteQueue()
    # q.deleteQueue()
    # q.deleteQueue()
    # q.printQueue()
    q.destroyQueue()