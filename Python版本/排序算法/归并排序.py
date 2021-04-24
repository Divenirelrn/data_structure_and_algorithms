#o(nlogn)

def merge(l, left, mid, right):
    l_arr = l[left:mid+1]
    r_arr = l[mid+1:right+1]

    k = left #BUG
    i = j = 0
    while(i < len(l_arr) and j < len(r_arr)):
        if l_arr[i] <= r_arr[j]:
            l[k] = l_arr[i]
            i += 1
        else:
            l[k] = r_arr[j]
            j += 1

        k += 1

    while(i < len(l_arr)):
        l[k] = l_arr[i]
        k += 1
        i += 1

    while (j < len(r_arr)):
        l[k] = r_arr[j]
        k += 1
        j += 1


def merge_sort(l, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(l, left, mid)
    merge_sort(l, mid+1, right)

    merge(l, left, mid, right)


if __name__ == "__main__":
    l = [10,3,5,6,1,2]
    merge_sort(l, 0, len(l)-1)
    print(l)