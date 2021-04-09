/*循环链表查找*/

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

void ds_search(Node* pNode, int elem)
{
	Node* target;
	int i = 1;
	
	for (target=pNode; target->data != elem && target->Next != pNode; ++i)
	{
		target = target->Next;
	}

	if (target->Next == pNode)
		return 0;
	else
		return 1;

}