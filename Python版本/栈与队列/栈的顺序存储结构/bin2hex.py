#二进制转十进制
import stack

def bin2hex():
    bin = input("Please input your number, ends with '#':")

    s = stack.Stack()
    for i in range(len(bin)-1):
        s.push(int(bin[i]))

    total = 0
    i = 0
    while(s.top != None):
        total += s.pop() * 2 ** (i)
        i += 1

    return total


if __name__ == "__main__":
    print(bin2hex())