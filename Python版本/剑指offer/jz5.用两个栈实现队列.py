# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.n1 = 0
        self.n2 = 0

    def push(self, node):
        # write code here
        self.stack1.append(node)
        self.n1 += 1

    def pop(self):
        # return xx
        if self.n2 != 0:
            self.n2 -= 1
            return self.stack2.pop()
        else:
            while self.n1 > 1:
                val = self.stack1.pop()
                self.n1 -= 1
                self.stack2.append(val)
                self.n2 += 1

            self.n1 -= 1
            return self.stack1.pop()
