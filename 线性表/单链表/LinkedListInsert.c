/*
�������˼·��
	����һ�����pָ������ͷ��㣬��ʼ��j��1��ʼ��
	��j<1ʱ���ͱ�����㣬��p��ָ������ƶ�������ָ����һ��㣬j�ۼ�1��
	��������ĩβpΪ�գ���˵����i��Ԫ�ز�����;
	������ҳɹ�����ϵͳ������һ���ս��;
	������Ԫ��e��ֵ��s->data;
	������Ĳ���ղ�������׼��䣻
	���سɹ���

*/

#include "���Ա�.c"

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