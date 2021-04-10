/*
问题描述：魔术师手里一共有13张牌，全是黑桃，1~13.
*********魔术师需要实现一个魔术：这是十三张牌全部放在桌面上（正面向下），
********第一次摸出第一张，是1，翻过来放在桌面上。
******第二次摸出从上往下数第二张，是2，翻过来 放在桌面上，（第一张放在最下面去，等会儿再摸），
*****第三次摸出从上往下数第三张，是3，翻过来放在桌面上，（第一张和第二张 放在最下面去，等会儿再摸）
***  以此类推 最后一张就是13
*/

#include <stdio.h>
#include <stdlib.h>

#define  CardNumber 13

typedef struct node
{
    int data;
    struct node* next;
}sqlist, * linklist;

linklist CreateLinkList()
{
    linklist head = NULL;
    linklist s, r;
    int i;

    r = head;

    for (i = 1; i <= CardNumber; i++)
    {
        s = (linklist)malloc(sizeof(sqlist));
        s->data = 0;

        if (head == NULL)
            head = s;
        else
            r->next = s;

        r = s;
    }

    r->next = head;

    return head;
}

// 发牌顺序计算
void Magician(linklist head)
{
    linklist p;
    int j;
    int Countnumber = 2;

    p = head;
    p->data = 1;  //第一张牌放1

    while (1)
    {
        for (j = 0; j < Countnumber; j++)
        {
            p = p->next;
            if (p->data != 0)  //该位置有牌的话,则下一个位置
            {
                p->next;
                j--;
            }
        }

        if (p->data == 0)
        {
            p->data = Countnumber;
            Countnumber++;

            if (Countnumber == 14)
                break;
        }
    }
}

// 销毁工作
void DestoryList(linklist* list)
j
}

int main()
{
    linklist p;
    int i;

    p = CreateLinkList();
    Magician(p);

    printf("按如下顺序排列：\n");
    for (i = 0; i < CardNumber; i++)
    {
        printf("黑桃%d ", p->data);
        p = p->next;
    }

    DestoryList(&p);

    return 0;
}
