
def b_s(l, val):
    """递归实现折半查找法"""
    if len(l) <= 0:
        print("not found")
        return

    center = len(l) // 2

    if l[center] == val:
        print("get")
        return
    elif l[center] > val:
        b_s(l[:center], val)
    else:
        b_s(l[center + 1:], val)


def b_s2(l, val):
    """迭代实现折半查找法"""
    length = len(l)
    left = 0
    right = length - 1

    while(left <= right):
        mid = (left + right) // 2

        if l[mid] == val:
            return mid

        elif l[mid] > val:
            right = mid - 1

        elif l[mid] < val:
            left = mid + 1

    return -1


if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10]
    # b_s(l, 11)
    print(b_s2(l, 0))