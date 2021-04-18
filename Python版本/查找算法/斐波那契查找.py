
def fib(n):
    f = [1,1]

    for i in range(2, n):
        f.append(f[i-1] + f[i - 2])

    return f


def fib_search(l, key):
    f = fib(20)
    left, right = 0, len(l) - 1

    k = 0
    while len(l) > f[k]-1:
        k += 1

    for i in range(len(l), f[k]-1):
        l.append(l[right])

    while(left <= right):
        mid = left + f[k-1] - 1
        if l[mid] < key:
            left = mid + 1
            k -= 2
        elif l[mid] > key:
            right = mid - 1
            k -= 1
        else:
            if mid <= right:
                return mid
            else:
                return right

    return -1


if __name__ == "__main__":
    l = [1, 5, 15, 22, 25, 31, 39, 42, 47, 49, 59, 68, 88]
    print(fib_search(l, 89))