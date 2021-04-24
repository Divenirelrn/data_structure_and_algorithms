
#尾递归

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def fast(l, left, right):
    mid = (left + right) // 2
    if l[left] > l[right]:
        swap(l, left, right)

    if l[mid] > l[right]:
        swap(l, mid, right)

    if l[left] < l[mid]:
        swap(l, left, mid)

    pivot = l[left]

    while left < right:
        while(left < right and l[right] >= pivot):
            right -= 1

        # swap(l, left, right)
        l[left] = l[right]

        while(left < right and l[left] <= pivot):
            left += 1

        # swap(l, left, right)
        l[right] = l[left]

    l[left] = pivot

    return left


def fast_sort(l, left, right):
    if left >= right:
        return

    i = fast(l, left, right)

    fast_sort(l, left, i-1)
    fast_sort(l, i+1, right)



if __name__ == "__main__":
    l = [10,3,5,6,1,2]
    fast_sort(l, 0, len(l) - 1)
    print(l)