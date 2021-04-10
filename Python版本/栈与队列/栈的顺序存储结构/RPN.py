from stack import Stack


def rpn(exp):
    """逆波兰表达式"""
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


def post2center(exp):
    """后缀表达式转中缀表达式"""
    res = ""
    s = Stack()
    for char in exp:
        print(char)
        if char == '(' or ord(char) >= 48 and ord(char) <= 57:
            s.push(char)
            s.printStack()
        elif char == ')':
            while(s.top != '(' and s.top != s.base):
                res += s.pop()
            s.pop()
            s.printStack()
        else:
            while(s.top != '(' and s.top != s.base):
                res += s.pop()
            s.push(char)
            s.printStack()

    res += s.pop()
    return res


if __name__ == "__main__":
    # print(rpn('53+23-*'))
    print(post2center("((1-2)*3+2)*((5+7)/(6-9)+2)"))