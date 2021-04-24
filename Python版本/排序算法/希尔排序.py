#在此之前，时间复杂度均为o(n^2)

def shell_sort(l):
    idx = len(l)
    while(idx > 1):
        idx = idx //3 + 1
        for i in range(idx, len(l)):
            j = i
            temp = l[i]
            while(j >= idx and temp < l[j-idx]):
                j -= idx

            if j != i:
                for k in range(i, j-idx, -idx):
                    l[k] = l[k-idx]

                l[j] = temp



if __name__ == "__main__":
    l = [49,38,65,97,76,13,27,49,55,4]
    shell_sort(l)
    print(l)



