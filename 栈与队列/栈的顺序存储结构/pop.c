//出栈操作

#include "栈与队列.c"

POP(sqStack* s, ElemType *e)
{
	if (s->top == s->base)
	{
		return;
	}
	*e = *--(s->top);
}