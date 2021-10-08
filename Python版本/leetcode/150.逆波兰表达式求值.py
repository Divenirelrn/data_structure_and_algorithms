
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n == 1:
            return int(tokens[0])

        stack = list()
        res = 0

        for i in range(n):
            if tokens[i] not in ('+', '-', '*', '/'):
                stack.append(tokens[i])
            else:
                x1 = int(stack.pop())
                x2 = int(stack.pop())

                if tokens[i] == '+':
                    res = x1 + x2
                elif tokens[i] == '-':
                    res = x2 - x1
                elif tokens[i] == '*':
                    res = x1 * x2
                elif tokens[i] == '/':
                    res = int(x2 / x1)

                stack.append(res)

        return res
