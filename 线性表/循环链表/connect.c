//两个链表连接

LinkList Connect(LinkList A, LinkList B)
{
	LinkList p = A->next;
	A->next = B -> next->next;
	free(B->next);
	B->next = p;
	return B;
}