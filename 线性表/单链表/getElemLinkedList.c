/*
�������ȡ˼·��
	����һ�����pָ�������һ����㣬��ʼ��j��1��ʼ��
	��j<iʱ���ͱ���������p��ָ������ƶ�������ָ����һ����㣬j+1;
	��������ĩβpΪ�գ���˵����i��Ԫ�ز����ڣ�
	������ҳɹ������ؽ��p�����ݡ�

����ʱ�临�Ӷ�Ϊo(n)��ƽ��Ϊo(n)

��֪��Ҫѭ�����ٴΣ���˲�������for��ʵ��

����˼���ǡ�����ָ����ơ�
*/

#include "���Ա�.c"

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