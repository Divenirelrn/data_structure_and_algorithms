/*
�������pָ���һ����㣬��ʼ��j=1;
��j<1ʱ������������p��ָ������ƶ�������ָ����һ����㣬j�ۼ�1;
��������ĩβpΪ�գ���˵����i��Ԫ�ز����ڣ�
������ҳɹ�������ɾ�����p->next��ֵ��q;
�������ɾ����׼���p->next = q->next;
��q����е����ݸ�ֵ��e,��Ϊ���أ�
�ͷ�q��㡣
*/

#include "���Ա�.c"

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