/*
�����㷨��˼·��
	�������λ�ò������׳��쳣
	������Ա��ȴ��ڵ������鳤�ȣ����׳��쳣��̬��������������
	�����һ��Ԫ�ؿ�ʼ��ǰ��������i��λ�ã��ֱ����Ƕ�����ƶ�һ��λ�ã�
	��Ҫ����Ԫ������λ��i����
	���Ա���+1.
*/

#include "���Ա�.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status ListInsert(SqList* L, int i, ElemType e)
{
	int k;

	if (L->length == MAXSIZE)
	{
		return ERROR;
	}
	if (i<1 || i>L->length+1)
	{
		return ERROR;
	}
	if (i <= L->length)
	{
		for (k=L->length-1; k>=i-1;k--)
		{
			L->data[k + 1] = L->data[k];
		}
	}

	L->data[i - 1] = e;
	L->length++;

	return OK;
}