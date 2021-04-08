/*
删除算法思路：
	如果删除位置不合理，抛出异常
	取出删除元素
	从删除元素位置开始遍历到最后一个元素位置，分别将它们向前移动一个位置
	表长-1

时间复杂度：
	最好o(1)，最坏o(n),平均o(n)
*/

#include "线性表.c"

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