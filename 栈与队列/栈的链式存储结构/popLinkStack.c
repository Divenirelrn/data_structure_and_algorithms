Status Pop(LinkStack* s, ElemType* e)
{
	LinkStackPtr p;
	if (StackEmpty(*s))  // �ж��Ƿ�Ϊ��ջ
		return ERROR;
	*e = s->top->data;
	p = s->top;
	s->top = s->top->next;
	free(p);
	s->count--;
	return OK;
}
