/*ѭ���������*/

#include "���Ա�.c"

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

	printf("������Ҫ�������ֵ");
	scanf("%d", &item);

	if (i == 1)
	{//�²�������Ϊ��һ�����
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