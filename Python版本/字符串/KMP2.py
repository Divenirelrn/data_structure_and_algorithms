
def get_next(substr):
    """
    next数组是PMT(partial match table)往后错一位，在第一位补-1，舍弃最后一位
    利用next数组代替PMT，是为了方便计算

    next数组的求法可以看成自身与自身匹配，在每一个位置看能匹配到的字符有几个
    如："ababcabaa"
    next[0] = -1
    a 最长匹配前后缀为0 因此PMT[0]=0, next[1]=0
    ab 最长匹配前后缀为0 因此PMT[1]=0, next[2]=0
    aba 最长匹配前后缀为1 因此PMT[2]=1, next[2]=1
    abab 最长匹配前后缀为2 因此PMT[2]=2, next[3]=2
    ......
    当找ab的最长前后缀时，将b与a进行比较;这相当于将b与ababcabaa（副串）的第一个元素a进行比较
    （由于找ab的最长前后缀时,a与b不等）当找aba的最长前后缀时，首先将a（aba的最后一个元素）与a进行比较;
    这相当于将a（aba的最后一个元素）与ababcabaa的第一个元素a进行比较
    （由于找aba的最长前后缀时,a与a相等）当找abab的最长前后缀时，相当于将b(abab的最后一个元素)与ababcabaa的第二个元素b进行比较
    ......
    """
    len_s = len(substr)
    next_arr = [None] * len_s
    next_arr[0] = -1
    i = 0
    j = -1

    while i < len_s - 1:
        if j == -1 or substr[i] == substr[j]:
            i += 1
            j += 1
            next_arr[i] = j
        else:
            j = next_arr[j]

    return next_arr


def KMP(string, substr):
    """
    KMP算法的精髓：
     当出现主串元素与子串元素不匹配是，就用子串的最长公共前缀去对齐主串的最长公共后缀

     PMT(Partial Mtach Table):
     char: a b a b a b c a
     index 0 1 2 3 4 5 6 7
     PMT   0 0 1 2 3 4 0 1
     next -1 0 0 1 2 3 4 0
    """
    next_arr = get_next(substr)
    i = j = 0
    len_s = len(string)
    len_sub = len(substr)
    while i < len_s and j < len_sub:
        if j == -1 or string[i] == substr[j]:
            i += 1
            j += 1
        else:
            j = next_arr[j]

    if j == len_sub:
        return i - j
    else:
        return -1


if __name__ == "__main__":
    # print(get_next("ababcabaa"))
    # print(KMP("ABABCABABCABAAB", "ABABCABAA"))
    print(KMP("hello", "ll"))