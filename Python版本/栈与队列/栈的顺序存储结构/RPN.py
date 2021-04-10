#逆波兰表达式
from stack import Stack


def rpn(exp):
    s = Stack()

    for char in exp:
        if ord(char) >= 48 and ord(char) <= 57:
            s.push(int(char))

        else:
            a = s.pop()
            b = s.pop()
            if char == '+':
                s.push(a + b)
            elif char == '-':
                s.push(b - a)
            elif char == '*':
                s.push(a * b)
            elif char == '/':
                s.push(b / a)

    return s.top


if __name__ == "__main__":
    print(rpn('53+23-*'))