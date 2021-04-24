
def select_sort(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i, len(l)):
            if l[j] < l[min]:
                min = j

        if min != i:
            temp = l[i]
            l[i] = l[min]
            l[min] = temp


if __name__ == "__main__":
    l = [2,5,1,8,4]
    select_sort(l)
    print(l)