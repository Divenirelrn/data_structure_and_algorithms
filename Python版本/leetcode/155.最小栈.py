
class MinStack:

    def __init__(self):
        self.cache = list()
        self.size = 0
        self.minValue = sys.maxsize

    def push(self, val: int) -> None:
        self.cache.append(val)
        self.size += 1
        if self.minValue > val:
            self.minValue = val

    def pop(self) -> None:
        val = self.cache.pop()
        self.size -= 1
        if val == self.minValue:
            self.minValue = sys.maxsize
            for i in range(self.size):
                if self.cache[i] < self.minValue:
                    self.minValue = self.cache[i]


    def top(self) -> int:
        return self.cache[-1]

    def getMin(self) -> int:
        return self.minValue



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()