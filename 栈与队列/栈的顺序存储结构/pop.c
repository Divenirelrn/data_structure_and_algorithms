//��ջ����

#include "ջ�����.c"

POP(sqStack* s, ElemType *e)
{
	if (s->top == s->base)
	{
		return;
	}
	*e = *--(s->top);
}