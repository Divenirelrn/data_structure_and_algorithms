/*
如果从文件中读取的数据记录的关键字是有序排列的，则可以用一种效率比较高的查找方法来查找文件的记录，这就是折半查找法，又称为二分法搜索。
折半查找的基本思想是：减小查找序列的长度，分而治之地进行关键字的查找。
折半查找的实现过程是：先确定待查找记录的所在范围，然后逐渐缩小这个范围，直到找到该记录或查找失败（查无该记录）为止。
例如有序列：1 1 2 3 5 8 13 21 34 55 89（该序列包含 11 个元素，而且关键字单调递增。），现要求查找关键字 key 为 55 的记录。
我们可以设指针 low 和 high 分别指向关键字序列的上界和下界，指针 mid 指向序列的中间位置，即 mid = (low+high)/2。
*/
// ********************************
// By 小甲鱼，http://www.fishc.com
// ********************************
#include <stdio.h>

int bin_search(int str[], int n, int key)
{
    int low, high, mid;

    low = 0;
    high = n - 1;

    while (low <= high)
    {
        mid = (low + high) / 2;
        if (str[mid] == key)
        {
            return mid;                // 查找成功
        }
        if (str[mid] < key)
        {
            low = mid + 1;        // 在后半序列中查找
        }
        if (str[mid] > key)
        {
            high = mid - 1;        // 在前半序列中查找
        }
    }

    return -1;                                // 查找失败
}

int main()
{
    int str[11] = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
    int n, addr;

    printf("请输入待查找的关键字: ");
    scanf("%d", &n);

    addr = bin_search(str, 11, n);
    if (-1 != addr)
    {
        printf("查找成功，可喜可贺，可口可乐! 关键字 %d 所在的位置是: %d\n", n, addr);
    }
    else
    {
        printf("查找失败!\n");
    }

    return 0;
}