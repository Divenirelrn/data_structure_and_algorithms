//课后作业，查找记录

#include <stdio.h>

typedef struct student
{
    int id;
    char name[10];
    float score;
}Student;

float search(Student stu[], int n, int key)
{
    int i;

    for (i = 0; i < n; i++)
    {
        if (stu[i].id == key)
        {
            return i.score;
        }
    }

    return -1;
}

int main()
{
    Student stu[4] = {
        {0000, "小甲鱼", 100},
        {0001, "风介", 99},
        {0002, "康小泡", 101},
        {0003, "不二如是", 33}
    };

    float score;

    score = search(stu, 4, 0002);
    printf("0002号康小泡大姐大的成绩是：%f", score);

    return 0;
}