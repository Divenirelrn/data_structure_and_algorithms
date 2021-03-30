/*
KMP算法改进
后来有人发现，KMP算法是有缺陷的。

比如我们的主串 ：
S =“aaaabcde”

子串 ：
T =“aaaaax”

其中很容易得到next数组为012345。

效率很低下，a不等于b，必须要改进。
next数组中添加回溯到前缀数字的索引。
*/

#include <stdio.h>

typedef char* String;

void get_next(String T, int* next)
{
    int j = 0;
    int i = 1;
    next[1] = 0;

    while (i < T[0])
    {
        if (0 == j || T[i] == T[j])
        {
            i++;
            j++;
            if (T[i] != T[j])
            {
                next[i] = j;
            }
            else
            {
                next[i] = next[j];
            }
        }
        else
        {
            j = next[j];
        }
    }
}

// 返回子串T在主串S第pos个字符之后的位置
// 若不存在，则返回0
int Index_KMP(String S, String T, int pos)
{
    int i = pos;
    int j = 1;
    int next[255];

    get_next(T, next);

    while (i <= S[0] && j <= T[0])
    {
        //增加判断，防止特殊情况发生
        if (0 == j || S[i] == T[j])
        {
            i++;
            j++;
        }
        else
        {
            j = next[j];
        }
    }

    if (j > T[0])
    {
        return i - T[0];
    }
    else
    {
        return 0;
    }
}
