/*
声明结点p指向第一个结点，初始化j=1;
当j<1时，遍历链表，让p的指针向后移动，不断指向下一个结点，j累加1;
若到链表末尾p为空，则说明第i个元素不存在；
否则查找成功，将欲删除结点p->next赋值给q;
单链表的删除标准语句p->next = q->next;
将q结点中的数据赋值给e,作为返回；
释放q结点。
*/

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status ListDelete(LinkList* L, int i, ElemType* e)
{
	int j;
	LinkList p,q;

	p = *L;
	j = 1;

	while (p->Next && j < i)
	{
		p = p->Next;
		++j;
	}

	if (!(p->Next) || j>i)
	{
		return ERROR;
	}

	q = p->Next;
	p->Next = q->Next;

	*e = q->data;
	free(q);

	return OK;

}