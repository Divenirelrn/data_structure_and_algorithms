/*��ʼ��ѭ������*/

#include "���Ա�.c"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

void ds_init(Node** pNode)
{
	int item;
	Node* temp;
	Node* target;

	printf("�������ֵ������0��ɳ�ʼ��\n");

	while (1)
	{
		scanf("%d", &item);
		fflush(stdin);

		if (item == 0)
			return;

		if ((*pNode == NULL))
		{
			*pNode = (Node*)malloc(sizeof(struct CLinkList));
			if (!(*pNode))
				exit(0);
			(*pNode)->data = item;
			(*pNode)->Next = *pNode;
		}
		else
		{
			/*�ҵ�nextָ���һ�����Ľ��*/
			for (target = (*pNode); target->Next != (*pNode); target = target->Next)
				;
			/*����һ���µĽ��*/
			temp = (Node*)malloc(sizeof(struct CLinkList));

			if(!temp)
				exit(0);

			temp->data = item;
			temp->Next = *pNode;
			target->Next = temp;

		}
	}
}