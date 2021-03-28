/*
插入算法的思路：
	如果插入位置不合理，抛出异常
	如果线性表长度大于等于数组长度，则抛出异常或动态增加数组容量；
	从最后一个元素开始向前遍历到第i个位置，分别将它们都向后移动一个位置；
	将要插入元素填入位置i处；
	线性表长度+1.
*/

#include "线性表.c"

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