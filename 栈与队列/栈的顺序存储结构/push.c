//入队操作


#include "栈与队列.c"

#define STACKINCREMENT 10

PUSH(sqStack *s, ElemType e)
{
	if (s->top - s->base >= s->stackSize)
	{
		s->base = (ElemType*)realloc(s->base, (s->stackSize + STACKINCREMENT) * sizeof(ElemType));
		if (!s->base)
			exit(0);

		s->top = s->base + s->stackSize;
		s->stackSize = s->stackSize + STACKINCREMENT;
	}
	*(s->top) = e;
	s->top++;
}