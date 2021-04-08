/*
单链表读取思路：
	声明一个结点p指向链表第一个结点，初始化j从1开始；
	当j<i时，就遍历链表，让p的指针向后移动，不断指向下一个结点，j+1;
	若到链表末尾p为空，则说明第i个元素不存在；
	否则查找成功，返回结点p的数据。

最坏情况时间复杂度为o(n)，平均为o(n)

不知道要循环多少次，因此不方便用for来实现

核心思想是“工作指针后移”
*/

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status GetElem(LinkList L, int i, ElemType* e)
{
	int j;
	LinkList p;

	p = L->Next;
	j = 1;

	while (p && j<i)
	{
		p = p->Next;
		++j;
	}

	if (!p || j>i)
	{
		return ERROR;
	}

	*e = p->data;

	return OK;
}