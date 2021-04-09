/*初始化循环链表*/

#include "线性表.c"

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

	printf("输入结点的值，输入0完成初始化\n");

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
			/*找到next指向第一个结点的结点*/
			for (target = (*pNode); target->Next != (*pNode); target = target->Next)
				;
			/*生成一个新的结点*/
			temp = (Node*)malloc(sizeof(struct CLinkList));

			if(!temp)
				exit(0);

			temp->data = item;
			temp->Next = *pNode;
			target->Next = temp;

		}
	}
}