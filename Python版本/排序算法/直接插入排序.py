#基本有序的情况下效率较高

def insert_sort(l):
    for i in range(1, len(l)):
        temp = l[i]
        j = i
        while(j >= 1 and temp < l[j-1]):
            j -= 1

        if j != i:
            for k in range(i, j-1, -1):
                l[k] = l[k-1]

            l[j] = temp


if __name__ == "__main__":
    l = [1,4,5,7,2,3,6,9,8,10]
    insert_sort(l)
    print(l)