
def bin_search(l, key):
    """二分查找"""
    left = 0
    right = len(l) - 1

    while(left <= right):
        mid = (left + right) // 2
        if l[mid] == key:
            return mid
        elif l[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def inter_search(l, key):
    """插值查找"""
    left = 0
    right = len(l) - 1

    while (left <= right):
        mid = left + ((key - l[left]) // (l[right] - l[left])) * (right - left)
        if l[mid] == key:
            return mid
        elif l[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10]
    print(bin_search(l, 11))
    print(inter_search(l, 1))