//编写一个递归函数，实现将输入的任意长度的字符串反向输出的功能。例如输入字符串FishC,则输出字符串ChsiF。

void print()
{
    char a;
    scanf(“ % c”, &a);
    if (a != ‘#’)  print();
    if (a != ‘#’)  printf(“ % c”, a);
}
