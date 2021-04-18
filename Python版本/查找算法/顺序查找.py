

def seq_search(l, key):
    """顺序查找"""
    for i in range(len(l)):
        if l[i] == key:
            return i

    return -1

def seq_search2(l, key):
    """顺序查找改进"""
    l[0] = key #哨兵
    i = len(l) - 1

    while(l[i] != key):
        i -= 1

    return i


if __name__ == "__main__":
    l = ['a','b','c','d','e']
    print(seq_search(l, 'b'))

    l2 = [None, 'a','b','c','d','e']
    print(seq_search2(l2, 'b'))