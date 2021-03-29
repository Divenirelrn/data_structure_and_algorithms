/*循环链表删除*/

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

void ds_delete(Node** pNode, int i)
{
	Node* temp;
	Node* target;
	int j = 1;

	if (i == 1)
	{
		for (target = (*pNode); target->Next != (*pNode); target = target->Next)
			;

		temp = *pNode;
		*pNode = (*pNode)->Next;
		target->Next = *pNode;
		free(temp);
	}
	else
	{
		target = *pNode;

		for (; j < (i - 1); ++j)
		{
			target = target->Next;
		}

		temp = target->Next;
		target->Next = temp -> Next;
		free(temp);
	}
}