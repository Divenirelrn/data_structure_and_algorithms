//尾插法

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

void createListTail(LinkList* L, int n)
{
	LinkList p, r;
	int i;

	srand(time(0));

	*L = (LinkList)malloc(sizeof(Node));
	r = *L;

	for (i = 0; i < n; i++)
	{
		p = (Node *)malloc(sizeof(Node));
		p->data = rand() % 100 + 1;
		p->Next = p;
		r = p;
	}
	r->Next = NULL;
}