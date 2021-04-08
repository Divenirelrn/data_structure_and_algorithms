//静态链表插入

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

int Malloc_SLL(StaticLinkList space)
//获得空闲分量的下标
{
	int i = space[0].cur;
	if (space[0].cur)
	{
		space[0].cur = space[i].cur;
	}
	return i;
}

Status ListInsert(StaticLinkList L, int i, ElemType e)
{
	int j, k, l;
	k = MAXSIZE - 1;
	if (i < 1 || i>ListLength(L) + 1)
	{
		return ERROR;
	}

	j = Malloc_SLL(L);
	if (j)
	{
		L[j].data = e;
		for (l=1; l<=i-1;l++)
		{
			k = L[k].cur;
		}
		L[j].cur = L[k].cur;
		L[k].cur = j;

		return OK;
	}

	return ERROR;
}

