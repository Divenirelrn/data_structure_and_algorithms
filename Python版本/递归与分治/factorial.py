

def fac(n):
    """计算n的阶乘"""
    if n == 1:
        return 1

    return n * fac(n-1)


if __name__ == "__main__":
    print(fac(6))
