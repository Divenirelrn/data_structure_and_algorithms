# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.contianer = []
        self.n = 0

    def Insert(self, num):
        # write code here
        if self.n == 0:
            self.contianer.append(num)
        else:
            self.contianer.append(num)
            j = self.n - 1
            while j >= 0 and self.contianer[j] > num:
                self.contianer[j + 1] = self.contianer[j]
                j -= 1
            self.contianer[j + 1] = num

        self.n += 1

    def GetMedian(self):
        # write code here
        if self.n % 2 != 0:
            return self.contianer[self.n // 2]
        else:
            return (self.contianer[self.n // 2] + self.contianer[self.n // 2 - 1]) / 2

#方法二：堆
# -*- coding:utf-8 -*-
from heapq import heappush, heappop


class Solution:
    def __init__(self):
        self.left = []
        self.right = []

    def Insert(self, num):
        heappush(self.left, -num)
        heappush(self.right, -heappop(self.left))

        if len(self.left) < len(self.right):
            heappush(self.left, -heappop(self.right))

    def GetMedian(self):
        # write code here
        if len(self.left) > len(self.right):
            res = -heappop(self.left)
            heappush(self.left, -res)
            return res
        else:
            res = heappop(self.right)
            res2 = -heappop(self.left)
            heappush(self.left, -res2)
            heappush(self.right, res)
            return (res + res2) / 2

