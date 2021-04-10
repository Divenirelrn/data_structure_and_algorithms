
class CycleQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.c = [None] * maxsize
        self.front = self.rear = 0

    def printQueue(self):
        temp = []
        i = self.front

        if self.front == self.rear:
            temp.append(self.c[i])
            i += 1

        while(i != self.rear):
            temp.append(self.c[i])
            i += 1
            i %= self.maxsize

        if self.front != self.rear:
            temp.append(self.c[i])
        print(temp)


    def insertQueue(self, val):
        if self.front == self.rear and self.c[self.front] != None:
            return -1

        self.c[self.rear] = val
        self.rear += 1
        self.rear %= self.maxsize

    def deleteQueue(self):
        if self.front == self.rear:
            return -1

        self.front += 1
        self.front %= self.maxsize


if __name__ == "__main__":
    cq = CycleQueue(10)

    cq.insertQueue(10)
    cq.insertQueue(20)
    cq.insertQueue(30)
    cq.deleteQueue()
    cq.insertQueue(40)
    cq.insertQueue(50)
    cq.insertQueue(60)
    cq.deleteQueue()
    cq.deleteQueue()
    cq.insertQueue(50)
    cq.insertQueue(60)
    cq.insertQueue(60)
    cq.insertQueue(60)
    cq.insertQueue(60)
    cq.insertQueue(60)
    cq.insertQueue(60)
    cq.insertQueue(60)
    cq.printQueue()