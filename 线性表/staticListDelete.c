//静态链表删除

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status ListDelete(StaticLinkList L, int i)
{
	int j, k;
	if (i<1 || i>ListLength(L))
	{
		return ERROR;
	}

	k = MAXSIZE - 1;

	for (j = 1; j <= i-1; j++)
	{
		k = L[k].cur;
	}

	j = L[k].cur;
	L[k].cur = L[j].cur;

	Free_SLL(L, j);

	return OK;
}


/*将下标为k的空闲结点回收到备用链表*/
void Free_SLL(StaticLinkList space, int k)
{
	space[k].cur = space[0].cur;
	space[0].cur = k;
}


/*返回元素个数*/
int ListLength(StaticLinkList L)
{
	int j = 0;
	int i = L[MAXSIZE - 1].cur;

	while (i)
	{
		i = L[i].cur;
		j++;
	}

	return j;
}