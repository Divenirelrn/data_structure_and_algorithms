/*
ɾ���㷨˼·��
	���ɾ��λ�ò������׳��쳣
	ȡ��ɾ��Ԫ��
	��ɾ��Ԫ��λ�ÿ�ʼ���������һ��Ԫ��λ�ã��ֱ�������ǰ�ƶ�һ��λ��
	��-1

ʱ�临�Ӷȣ�
	���o(1)���o(n),ƽ��o(n)
*/

#include "���Ա�.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status ListDelete(SqList* L, int i, ElemType* e)
{
	int k;
	if (L -> length == 0)
	{
		return ERROR;
	}
	if (i<1 || i>L->length)
	{
		return ERROR;
	}

	*e = L->data[i - 1];

	if (i < L->length)
	{
		for (k = i; k < L->length; k++)
		{
			L->data[k - 1] = L->data[k];
		}
	}

	L->length--;
	return OK;
}