#查找字符串，BF算法（回溯思想）
def bf(string, substr):
    for i in range(len(string) - len(substr) + 1):
        if string[i] == substr[0]:
            temp = i
            flag = True
            for j in range(1, len(substr)):
                if string[i + 1] != substr[j]:
                    flag = False
                    break

                i += 1

            if flag:
                return temp

            i = temp

    return -1



if __name__ == "__main__":
    print(bf("hello xiaojun", "h"))