
def move(n, x, y, z):
    if n == 1:
        print(x, "->", z)
    else:
        move(n - 1, x, z, y)
        print(x, "->", z)
        move(n-1, y, x, z)


if __name__ == "__main__":
    move(3, 'x', 'y', 'z')