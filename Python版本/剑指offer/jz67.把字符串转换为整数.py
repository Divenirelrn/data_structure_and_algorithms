#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Automaton:
    maxValue = 2 ** 31 - 1
    minValue = -2 ** 31

    def __init__(self):
        self.state = 'start'
        self.res = 0
        self.sign = 1
        self.stateDict = [['start', 'signed', 'number', 'end'],
                          ['end', 'end', 'number', 'end'],
                          ['end', 'end', 'number', 'end'],
                          ['end', 'end', 'end', 'end']]

    def getRow(self, state):
        if state == 'start':
            return 0
        elif state == 'signed':
            return 1
        elif state == 'number':
            return 2
        else:
            return 3

    def getState(self, c):
        stateLine = self.stateDict[self.getRow(self.state)]
        if c == ' ':
            self.state = stateLine[0]
        elif c == '+' or c == '-':
            self.state = stateLine[1]
        elif c.isdigit():
            self.state = stateLine[2]
        else:
            self.state = stateLine[3]

    def getResult(self, s):
        for c in s:
            self.getState(c)
            if self.state == 'signed':
                self.sign = -1 if c == '-' else self.sign
            elif self.state == 'number':
                self.res = self.res * 10 + int(c)

        self.res = min(self.res, self.maxValue) if self.sign == 1 else min(self.res, -self.minValue)
        return self.sign * self.res


class Solution:
    def StrToInt(self, s: str) -> int:
        # write code here
        autoMaton = Automaton()
        return autoMaton.getResult(s)


