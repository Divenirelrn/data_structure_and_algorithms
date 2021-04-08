//头插法

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

void createListHead(LinkList* L, int n)
{
	LinkList p;
	int i;

	srand(time(0));

	*L = (LinkList)malloc(sizeof(Node));
	(*L)->Next = NULL;

	for (i = 0; i < n; i++)
	{
		p = (LinkList)malloc(sizeof(Node));
		p->data = rand() % 100 + 1;
		p->Next = (*L)->Next;
		(*L)->Next = p;
	}
}