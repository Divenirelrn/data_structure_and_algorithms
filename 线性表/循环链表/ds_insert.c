/*循环链表插入*/

#include "线性表.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

void ds_insert(Node **pNode, int i)
{
	Node* temp;
	Node* target;
	Node* p;
	int item;
	int j = 1;

	printf("请输入要插入结点的值");
	scanf("%d", &item);

	if (i == 1)
	{//新插入结点作为第一个结点
		temp = (node*)malloc(sizeof(struct CLinkList));

		if (!temp)
			exit(0);

		temp->data = item;

		for (target = (*pNode);target->Next != (*pNode); target = target->Next)
			;
	
		temp->Next = (*pNode);
		target->Next = temp;
		*pNode = temp;
	}
	else
	{
		target = *pNode;

		for (; j < (i - 1); ++j)
		{
			target = target->Next;
		}

		temp = (Node*)malloc(sizeof(struct CLinkList));

		if (!temp)
			exit(0);

		temp->data = item;
		p = target->Next;
		target->Next = temp;
		temp->Next = p;
	}
}