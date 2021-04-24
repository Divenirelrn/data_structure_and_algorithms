
def bubble_sort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

def bubble_sort2(l):
    """冒泡排序优化"""
    flag = True
    for i in range(len(l) - 1, 0, -1):
        if not flag:
            break

        flag = False
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
                flag = True


if __name__ == "__main__":
    l = [1,4,5,7,2,3,6,9,8,10]
    # bubble_sort(l)
    bubble_sort2(l)
    print(l)
