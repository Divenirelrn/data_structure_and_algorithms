# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = list()
        self.minStack = list()
        self.minVal = 10001

    def push(self, node):
        # write code here
        self.stack.append(node)
        if node < self.minVal:
            self.minStack.append(node)
            self.minVal = node
        else:
            self.minStack.append(self.minVal)

    def pop(self):
        # write code here
        self.stack.pop()
        self.minStack.pop()
        self.minVal = self.minStack[-1]

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]