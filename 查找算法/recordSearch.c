//�κ���ҵ�����Ҽ�¼

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
        {0000, "С����", 100},
        {0001, "���", 99},
        {0002, "��С��", 101},
        {0003, "��������", 33}
    };

    float score;

    score = search(stu, 4, 0002);
    printf("0002�ſ�С�ݴ���ĳɼ��ǣ�%f", score);

    return 0;
}