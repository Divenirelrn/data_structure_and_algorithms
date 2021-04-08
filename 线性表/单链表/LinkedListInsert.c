/*
插入操作思路：
	声明一个结点p指向链表头结点，初始化j从1开始；
	当j<1时，就遍历结点，让p的指针向后移动，不断指向下一结点，j累加1；
	若到链表末尾p为空，则说明第i个元素不存在;
	否则查找成功，在系统中生成一个空结点;
	将数据元素e赋值给s->data;
	单链表的插入刚才两个标准语句；
	返回成功。

*/

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status ListInsert(LinkList *L, int i, ElemType e)
{
	int j;
	LinkList p, s;

	p = *L;
	j = 1;

	while (p && j < i)
	{
		p = p->Next;
		j++;
	}

	if (!p || j>i)
	{
		return ERROR;
	}

	s = (LinkList)malloc(sizeof(Node));
	s->data = e;

	s->Next = p->Next;
	p->Next = s;

	return OK;

}