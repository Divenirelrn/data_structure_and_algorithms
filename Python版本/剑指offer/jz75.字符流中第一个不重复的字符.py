# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.casein = set()
        self.onceElems = []

    def FirstAppearingOnce(self):
        # write code here
        return self.onceElems[0] if len(self.onceElems) else '#'

    def Insert(self, char):
        # write code here
        if char not in self.casein:
            self.casein.add(char)
            self.onceElems.append(char)
        elif char in self.onceElems:
            self.onceElems.remove(char)
