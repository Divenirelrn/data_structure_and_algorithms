//��Ѷ�����⣺��ȡ�м���

#include "���Ա�.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status GetMidNode(LinkList L, ElemType *e)
{
	LinkList search, mid;
	mid = search = L;

	while (search->Next != NULL)
	{
		if (search->Next->Next != NULL)
		{
			search = search->Next->Next;
			mid = mid->Next;
		}
		else
		{
			search = search->Next;
		}
		
	}

	*e = mid->Next;
	return OK;
}