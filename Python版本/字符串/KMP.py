
def get_next(string):
    next_arr = [None] * len(string)
    j = 0
    i = 1
    next_arr[1] = 0

    while(i < string[0]):
        if j == 0 or string[i] == string[j]:
            i += 1
            j += 1
            next_arr[i] = j

        else:
            j = next_arr[j]

    return next_arr

def get_next_advanced(string):
    """
    KMP算法改进
    aaaabcde
    aaaaax
    """
    next_arr = [None] * len(string)
    j = 0
    i = 1
    next_arr[1] = 0

    while(i < string[0]):
        if j == 0 or string[i] == string[j]:
            i += 1
            j += 1

            if string[i] != string[j]:
                next_arr[i] = j
            else:
                next_arr[i] = next_arr[j]

        else:
            j = next_arr[j]

    return next_arr


def KMP(str_arr, sub_arr, pos):
    next_arr = get_next(sub_arr)
    print(next_arr)
    i, j = pos, 1

    while(i <= str_arr[0] and j <= sub_arr[0]):
        if j == 0 or str_arr[i] == sub_arr[j]:
            i += 1
            j += 1
        else:
            j = next_arr[j]

    if j > sub_arr[0]:
        return i - sub_arr[0]
    else:
        return -1


if __name__ == "__main__":
    # print(get_next([9, 'a', 'b', 'a', 'b', 'a', 'a', 'a', 'b', 'a']))
    print(KMP([8, 'a', 'b', 'a', 'a', 'b', 'a', 'b', 'a'], [2, 'a', 'a'], 1))

