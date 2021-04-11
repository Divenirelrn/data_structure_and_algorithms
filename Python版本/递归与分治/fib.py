
def fib(n):
    """迭代法实现斐波那契数列"""
    a, b = 0, 1
    print(b)

    for _ in range(n-1):
        a, b = b, a + b
        print(b)


def fib2(n):
    """递归实现斐波那契数列"""
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fib2(n - 1) + fib2(n - 2)



if __name__ == "__main__":
    # fib(40)
    print(fib2(5))