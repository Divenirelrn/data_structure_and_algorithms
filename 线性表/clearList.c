//整表删除

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status clearList(LinkList* L)
{
	LinkList p, q;

	p = (*L)->Next;

	while (p)
	{
		q = p->Next;
		free(p);
		p = q;
	}

	(*L)->Next = NULL;
	return OK;

}